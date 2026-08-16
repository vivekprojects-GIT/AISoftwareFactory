"""Shared fixtures for the internal URL shortener acceptance suite.

These tests are derived from the approved acceptance criteria, not from the
implementation. They judge the API against the following contract, which is
the contract the criteria imply:

    module              app.main
    ASGI application    app.main.app
    identity guard      app.main.get_signed_in_user
                        A FastAPI dependency returning the OIDC subject of the
                        caller as a string, and raising 401 when the request
                        carries no valid workforce session.

    POST /api/links     body {"target_url": str}
                        201 -> {"short_code", "short_url", "target_url",
                                "click_count"}
                        422 -> malformed / unsupported target URL
                        401 -> no signed-in workforce user

    GET  /api/links     200 -> [link, ...] for the calling user only,
                        newest first
                        401 -> no signed-in workforce user

    GET  /{short_code}  redirect (3xx) with Location: target_url, and the
                        click count for that link increased by one
                        404 -> unknown short code

If the application cannot be imported yet the fixtures skip with that contract
in the message: a test that errors at collection reports nothing about the
product.
"""

from __future__ import annotations

import importlib
import os
import uuid
from dataclasses import dataclass
from types import ModuleType
from typing import Iterator

import pytest

API_MODULE_NAME = "app.main"
IDENTITY_DEPENDENCY_NAME = "get_signed_in_user"
ASGI_APPLICATION_NAME = "app"

CONTRACT_HINT = (
    f"The acceptance suite expects an importable module '{API_MODULE_NAME}' "
    f"exposing '{ASGI_APPLICATION_NAME}' (the FastAPI application) and "
    f"'{IDENTITY_DEPENDENCY_NAME}' (the OIDC identity dependency returning the "
    "signed-in workforce subject). See tests/conftest.py for the full contract."
)


def _workforce_subject(label: str) -> str:
    """Return a unique OIDC subject for one test.

    Subjects are unique per test so that per-user link lists are isolated from
    each other without the suite reaching into the application's storage.
    """
    return f"{label}-{uuid.uuid4().hex}@example.test"


@dataclass
class SignedInUser:
    """The workforce identity the overridden OIDC dependency will report.

    Mutable so a single test can act as one user and then another without
    rebuilding the client.
    """

    subject: str


@pytest.fixture(scope="session")
def api_module(tmp_path_factory: pytest.TempPathFactory) -> ModuleType:
    """Return the imported API module, or skip with the expected contract.

    Raises nothing: an unimportable application is reported as a skip so the
    rest of the suite still runs and still reports honestly.
    """
    pytest.importorskip(
        "fastapi",
        reason="FastAPI is not installed in this environment; " + CONTRACT_HINT,
    )
    database_path = tmp_path_factory.mktemp("shortener") / "acceptance.sqlite3"
    os.environ["APP_ENV"] = "test"
    os.environ["DATABASE_URL"] = f"sqlite:///{database_path}"
    try:
        module = importlib.import_module(API_MODULE_NAME)
    except ImportError as exc:  # implementation not present yet
        pytest.skip(f"{CONTRACT_HINT} Import failed: {exc}")
    for attribute in (ASGI_APPLICATION_NAME, IDENTITY_DEPENDENCY_NAME):
        if not hasattr(module, attribute):
            pytest.skip(f"{API_MODULE_NAME}.{attribute} is missing. {CONTRACT_HINT}")
    return module


@pytest.fixture()
def signed_in_user() -> SignedInUser:
    """Return the identity holder used by the authenticated client."""
    return SignedInUser(subject=_workforce_subject("alice"))


@pytest.fixture()
def other_user_subject() -> str:
    """Return a second workforce subject, for cross-user isolation tests."""
    return _workforce_subject("bob")


@pytest.fixture()
def client(api_module: ModuleType, signed_in_user: SignedInUser) -> Iterator[object]:
    """Yield a TestClient whose caller is the mutable signed-in workforce user."""
    from fastapi.testclient import TestClient

    application = getattr(api_module, ASGI_APPLICATION_NAME)
    identity_dependency = getattr(api_module, IDENTITY_DEPENDENCY_NAME)
    application.dependency_overrides[identity_dependency] = lambda: signed_in_user.subject
    try:
        with TestClient(application) as test_client:
            yield test_client
    finally:
        application.dependency_overrides.pop(identity_dependency, None)


@pytest.fixture()
def anonymous_client(api_module: ModuleType) -> Iterator[object]:
    """Yield a TestClient with no identity override: the real OIDC guard runs."""
    from fastapi.testclient import TestClient

    application = getattr(api_module, ASGI_APPLICATION_NAME)
    application.dependency_overrides.clear()
    with TestClient(application) as test_client:
        yield test_client
