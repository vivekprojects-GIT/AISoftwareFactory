// Import necessary hooks and components from React and other libraries
import React, { useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import QueryGenerator from './components/QueryGenerator';

// Define the main application component
const App: React.FC = () => {
  // Effect to initialize any necessary state or side effects
  useEffect(() => {
    // Initialization code here
  }, []);

  return (
    <Router>
      <Routes>
        <Route path='/' element={<QueryGenerator />} />
      </Routes>
    </Router>
  );
};

export default App;