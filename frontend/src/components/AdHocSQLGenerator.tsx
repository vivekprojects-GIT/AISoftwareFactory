// AdHocSQLGenerator.tsx
import React, { useState, useEffect } from 'react';
import { Button, Input, Textarea, Box, VStack, HStack, Spinner } from '@chakra-ui/react';
import axios from 'axios';

interface Question {
  id: number;
  question: string;
  answer: string;
  sql: string;
}

const AdHocSQLGenerator = () => {
  const [question, setQuestion] = useState('');
  const [answers, setAnswers] = useState<Question[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Load saved conversations from local storage or API
    const savedConversations = localStorage.getItem('conversations');
    if (savedConversations) {
      setAnswers(JSON.parse(savedConversations));
    }
  }, []);

  const handleQuestionChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setQuestion(e.target.value);
  };

  const handleSubmit = async () => {
    if (!question) return;

    setLoading(true);
    setError(null);

    try {
      const response = await axios.post('/api/generate-sql', { question });
      setAnswers([...answers, { id: Date.now(), question, answer: response.data.answer, sql: response.data.sql }]);
      localStorage.setItem('conversations', JSON.stringify([...answers, { id: Date.now(), question, answer: response.data.answer, sql: response.data.sql }]));
    } catch (err) {
      setError(err.response ? err.response.data.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box p={4} bg='white' shadow='md'>
      <VStack spacing={4} align='stretch'>
        {loading && <Spinner />}
        {error && <Text color='red'>{error}</Text>}
        <Textarea value={question} onChange={handleQuestionChange} placeholder='Ask a question in plain English...' />
        <Button onClick={handleSubmit} isDisabled={!question}>Generate SQL</Button>
        {answers.map((ans) => (
          <Box key={ans.id} p={2} border='1px solid #ccc' borderRadius='md'>
            <HStack justifyContent='space-between'>
              <Text fontWeight='bold'>{ans.question}</Text>
              <Text>{new Date().toLocaleString()}</Text>
            </HStack>
            <Text>Answer: {ans.answer}</Text>
            <CodeBlock language='sql'>{ans.sql}</CodeBlock>
          </Box>
        ))}
      </VStack>
    </Box>
  );
};

export default AdHocSQLGenerator;
