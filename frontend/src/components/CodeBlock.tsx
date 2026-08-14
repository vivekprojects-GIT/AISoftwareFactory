// CodeBlock.tsx
import React from 'react';
import { Box, Text } from '@chakra-ui/react';

interface CodeBlockProps {
  language: string;
  children: string;
}

const CodeBlock = ({ language, children }: CodeBlockProps) => {
  return (
    <Box p={4} bg='gray.50' borderRadius='md'>
      <Text fontFamily='monospace'>{children}</Text>
    </Box>
  );
};

export default CodeBlock;