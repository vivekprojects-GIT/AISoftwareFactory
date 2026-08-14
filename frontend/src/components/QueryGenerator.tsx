// Import necessary libraries and components
import React, { useState, useEffect } from 'react';
import { Button, Input, Textarea, Box, VStack, HStack, Spinner } from '@chakra-ui/react';
import axios from 'axios';

// Define the component
const QueryGenerator: React.FC = () => {
  const [question, setQuestion] = useState<string>('');
  const [sqlQuery, setSqlQuery] = useState<string>('\n');
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Function to handle question submission
  const handleSubmit = async () => {
    if (!question) return;
    setLoading(true);
    try {
      const response = await axios.post('/api/generate_sql', { question });
      setSqlQuery(response.data.sql_query);
      setError(null);
    } catch (err) {
      setError('Failed to generate SQL query.');
    } finally {
      setLoading(false);
    }
  };

  // Render the component
  return (
    <Box p={4} bg='white' borderRadius='md' shadow='sm'>
      <VStack spacing={4} align='stretch'>
        <Input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder='Ask a question in plain English'
          isRequired
        />
        {loading ? (
          <Spinner size='md' /> // Loading state
        ) : error ? (
          <Text color='red'>{error}</Text> // Error state
        ) : sqlQuery ? (
          <Textarea value={sqlQuery} readOnly rows={10} /> // Success state
        ) : null}
        <Button onClick={handleSubmit} isDisabled={!question || loading}>Generate SQL</Button>
      </VStack>
    </Box>
  );
};

export default QueryGenerator;