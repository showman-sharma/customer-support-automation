import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './Dashboard';
import EmailDetails from './EmailDetails';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/email/:id" element={<EmailDetails />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
