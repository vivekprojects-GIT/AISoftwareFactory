// Import necessary libraries and components
import React from 'react';
import QueryForm from './components/QueryForm';

// Define the main App component
const App: React.FC = () => {
  return (
    <div className='App'>
      <header className='App-header'>
        <h1>AI Software Factory</h1>
      </header>
      <main>
        <QueryForm />
      </main>
    </div>
  );
};

export default App;