import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [email, setEmail] = useState('');
  const [issue, setIssue] = useState('');
  const [issues, setIssues] = useState([]);

  useEffect(() => {
    fetchIssues();
  }, []);

  const fetchIssues = async () => {
    const response = await axios.get('http://localhost:5000/issues');
    setIssues(response.data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post('http://localhost:5000/submit', { email, issue });
    fetchIssues();
    setEmail('');
    setIssue('');
  };

  const handleSolve = async (issueId) => {
    await axios.post(`http://localhost:5000/solve/${issueId}`);
    fetchIssues();
  };

  const handleUnsolve = async (issueId) => {
    await axios.post(`http://localhost:5000/unsolve/${issueId}`);
    fetchIssues();
  };

  return (
    <div className="container">
      <h1 className="heading">Issue Tracker</h1>
      <form className="form-container" onSubmit={handleSubmit}>
        <input
          type="email"
          className="input-field"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
        />
        <input
          type="text"
          className="input-field"
          value={issue}
          onChange={(e) => setIssue(e.target.value)}
          placeholder="Issue"
          required
        />
        <button type="submit" className="submit-btn">Submit</button>
      </form>
      <h2 className="heading">Issues</h2>
      <ul className="issues-list">
        {issues.map((issue) => (
          <li key={issue._id} className="issue-item">
            <div>
              {issue.email} - {issue.issue} - {issue.status}
            </div>
            <div className="btn-container">
              <button className="solve-btn" onClick={() => handleSolve(issue._id)}>Solved</button>
              <button className="unsolve-btn" onClick={() => handleUnsolve(issue._id)}>Unsolved</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
