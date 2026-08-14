// Import necessary libraries and components
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, Input, Textarea, Box, VStack, Heading, Spinner } from '@chakra-ui/react';

// Define the component
const QueryGenerator: React.FC = () => {
  const [question, setQuestion] = useState('');
  const [sqlQuery, setSqlQuery] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Function to handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post('/api/generate-query', { question });
      setSqlQuery(response.data.sqlQuery);
    } catch (err) {
      setError('Failed to generate query. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Render the component
  return (
    <Box p={4} maxW='md' mx='auto'>
      <Heading mb={4}>Ask a Question</Heading>
      <form onSubmit={handleSubmit}>
        <Textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder='Enter your question here'
          mb={4}
        />
        <Button type='submit' colorScheme='blue' isLoading={loading}>Submit</Button>
      </form>
      {loading && <Spinner mt={4} />}
      {error && <Text mt={4} color='red'>{error}</Text>}
      {sqlQuery && (
        <Box mt={4} p={2} border='1px solid #ccc' borderRadius='md'>
          <Heading size='sm'>Generated SQL Query</Heading>
          <pre>{sqlQuery}</pre>
        </Box>
      )}
    </Box>
  );};

export default QueryGenerator;