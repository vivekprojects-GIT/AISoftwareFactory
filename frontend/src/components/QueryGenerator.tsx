// Import necessary hooks and components from React and other libraries
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, Input, Textarea, Box, VStack, HStack, Spinner } from '@chakra-ui/react';

// Define the component
const QueryGenerator: React.FC = () => {
  const [question, setQuestion] = useState('');
  const [sqlQuery, setSqlQuery] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  // Function to handle the query generation
  const generateQuery = async () => {
    if (!question) return;
    try {
      setLoading(true);
      const response = await axios.post('/api/generate-query', { question });
      setSqlQuery(response.data.sqlQuery);
      setError(null);
    } catch (err: any) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  // Render the component based on state
  return (
    <Box p={4} bg='white' borderRadius='md' shadow='sm'>
      <VStack spacing={4} align='stretch'>
        <Input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder='Ask a question in plain English'
          isRequired
        />
        <Button onClick={generateQuery} isLoading={loading} isDisabled={!question}>Generate SQL</Button>
        {error && <Text color='red'>{error.message}</Text>}
        {sqlQuery && (
          <VStack spacing={2} align='stretch'>
            <Text fontWeight='bold'>Generated SQL:</Text>
            <Textarea value={sqlQuery} isReadOnly rows={10} />
          </VStack>
        )}
      </VStack>
    </Box>
  );
};

export default QueryGenerator;