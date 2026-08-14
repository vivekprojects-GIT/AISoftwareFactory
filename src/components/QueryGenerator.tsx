// Import necessary hooks and components from React and other libraries
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, Input, Textarea, Alert } from '@design-system/components';

// Define the component's props interface
interface QueryGeneratorProps {
  onQueryGenerated: (sql: string) => void;
}

// Define the component's state interface
interface QueryGeneratorState {
  question: string;
  sql: string;
  loading: boolean;
  error: string | null;
}

// Define the component's initial state
const initialState: QueryGeneratorState = {
  question: '',
  sql: '',
  loading: false,
  error: null,
};

// Define the component's implementation
const QueryGenerator: React.FC<QueryGeneratorProps> = ({ onQueryGenerated }) => {
  const [state, setState] = useState<QueryGeneratorState>(initialState);

  // Handle changes to the question input field
  const handleQuestionChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setState({ ...state, question: event.target.value });
  };

  // Handle form submission
  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setState({ ...state, loading: true, error: null });

    try {
      const response = await axios.post('/api/generate-sql', { question: state.question });
      setState({ ...state, sql: response.data.sql, loading: false });
      onQueryGenerated(response.data.sql);
    } catch (error) {
      setState({ ...state, error: 'Failed to generate SQL query.', loading: false });
    }
  };

  // Render the component's UI
  return (
    <div>
      {state.error && <Alert type=