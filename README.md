# AISoftwareFactory

This repository is intended to implement a local SQL query generation service for analysts. The API contract requires the following:
- A question in plain English returns an answer and the SQL that produced it.
- Generated queries that would write or delete data are refused, not executed.
- Conversations are saved and can be reopened later with their questions and answers.