// Import necessary libraries
import React, { useState, useEffect } from 'react';
import './App.css';

// Define the main component
const App: React.FC = () => {
  const [question, setQuestion] = useState<string>('');
  const [sqlQuery, setSqlQuery] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Function to handle question submission
  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await fetch('/api/generate_sql', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question })
      });

      if (!response.ok) {
        throw new Error('Failed to generate SQL query');
      }

      const data = await response.json();
      setSqlQuery(data.sql);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className='App'>
      <header className='App-header'>
        <h1>SQL Query Generator</h1>
      </header>
      <main>
        <form onSubmit={handleSubmit}>
          <label htmlFor='question'>Ask a question:</label>
          <input
            type='text'
            id='question'
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button type='submit' disabled={loading}>Generate SQL</button>
        </form>
        {loading && <p>Loading...</p>}
        {error && <p>Error: {error}</p>}
        {sqlQuery && <pre>{sqlQuery}</pre>}
      </main>
    </div>
  );
};

export default App;