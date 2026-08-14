// Import necessary libraries and components
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, Input, Textarea, Box, VStack, HStack, Spinner } from '@chakra-ui/react';

// Define the component
const QueryGenerator: React.FC = () => {
  const [question, setQuestion] = useState('');
  const [sqlQuery, setSqlQuery] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
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
      setError('Failed to generate SQL query. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Render the component
  return (
    <Box p={4} borderWidth='1px' borderRadius='lg'>
      <VStack spacing={4} align='stretch'>
        <Input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder='Ask a question in plain English'
        />
        {loading && <Spinner />}
        {error && <Text color='red'>{error}</Text>}
        {sqlQuery && (
          <VStack spacing={2} align='stretch'>
            <Text fontWeight='bold'>Generated SQL Query:</Text>
            <Textarea value={sqlQuery} isReadOnly />
          </VStack>
        )}
        <Button onClick={handleSubmit} disabled={!question || loading}>Generate SQL</Button>
      </VStack>
    </Box>
  );
};

export default QueryGenerator;