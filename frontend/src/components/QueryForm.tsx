// Import necessary libraries and components
import React, { useState } from 'react';
import axios from 'axios';
import { Button, Input, Textarea, Box, VStack } from '@chakra-ui/react';

// Define the component
const QueryForm: React.FC = () => {
  const [question, setQuestion] = useState('');
  const [sqlQuery, setSqlQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Function to handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await axios.post('/api/query', { question });
      setSqlQuery(response.data.sqlQuery);
    } catch (err) {
      setError('An error occurred while processing your request.');
    } finally {
      setLoading(false);
    }
  };

  // Render the component
  return (
    <Box p={4} borderWidth='1px' borderRadius='lg'>
      <form onSubmit={handleSubmit}>
        <VStack spacing={4} align='stretch'>
          <Textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder='Ask a question in plain English'
            isRequired
          />
          <Button type='submit' colorScheme='blue' isLoading={loading}>Submit</Button>
        </VStack>
      </form>
      {error && <Text color='red'>{error}</Text>}
      {sqlQuery && <Text>{sqlQuery}</Text>}
    </Box>
  );
};

export default QueryForm;