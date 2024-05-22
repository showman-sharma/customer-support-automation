import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './Dashboard';
import EmailDetails from './EmailDetails';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/email/:id" element={<EmailDetails />} />
      </Routes>
    </Router>
  );
}

export default App;
