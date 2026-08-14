// Import necessary libraries and components
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import QueryGenerator from './components/QueryGenerator';

// Define the main application component
const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<QueryGenerator />} />
      </Routes>
    </Router>
  );
};

export default App;