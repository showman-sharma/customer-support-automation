import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTachometerAlt, faBox, faUsers, faDollarSign, faBullhorn, faQuestionCircle, faEnvelope, faCheckCircle, faTimesCircle } from '@fortawesome/free-solid-svg-icons';


import './App.css';
import './Dashboard.css';

function Dashboard() {
  const [searchTerm, setSearchTerm] = useState('');
  const [emails, setEmails] = useState([]);
  const [filterStatus, setFilterStatus] = useState('all');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchEmails = async () => {
      try {
        const response = await axios.get('http://localhost:5000/emails');
        setEmails(response.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchEmails();
  }, []);

  const filteredEmails = emails.filter(email => {
    const matchesSearchTerm = email.subject.toLowerCase().includes(searchTerm.toLowerCase());
    if (filterStatus === 'active') {
      return email.status === 'Solved' && matchesSearchTerm;
    } else if (filterStatus === 'inactive') {
      return email.status === 'Unsolved' && matchesSearchTerm;
    }
    return matchesSearchTerm;
  });

  const handleViewEmail = (email) => {
    navigate(`/email/${email.email}`);
  };

  const handleFilterChange = (status) => {
    setFilterStatus(status);
  };

  return (
    <div className="dashboard">
      <div className="sidebar">
        <h2>Dashboard</h2>
        <ul>
          <li><FontAwesomeIcon icon={faTachometerAlt} /> Overview</li><br />
          <li><FontAwesomeIcon icon={faBox} /> Products</li><br />
          <li className="active"><FontAwesomeIcon icon={faUsers} /> Customers</li><br />
          <li><FontAwesomeIcon icon={faDollarSign} /> Income</li><br />
          <li><FontAwesomeIcon icon={faBullhorn} /> Promote</li><br />
          <li><FontAwesomeIcon icon={faQuestionCircle} /> Help</li>
        </ul>
        
      </div>
      <div className="main-content">
        <header>
          <h1>Hello👋</h1>
          <div className="search-bar">
            <input 
              type="text" 
              placeholder="Search for emails..." 
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>
        </header>
        <div className="stats">
  <div className="stat">
    <FontAwesomeIcon icon={faEnvelope} size="2x" style={{ color: '#005a8d', marginRight: '10px' }} />
    <div>
      <p>Total Emails</p>
      <h2>{emails.length}</h2>
    </div>
  </div>
  <div className="stat">
    <FontAwesomeIcon icon={faCheckCircle} size="2x" style={{ color: '#4caf50', marginRight: '10px' }} />
    <div>
      <p>Solved</p>
      <h2>{emails.filter(email => email.status === 'Solved').length}</h2>
    </div>
  </div>
  <div className="stat">
    <FontAwesomeIcon icon={faTimesCircle} size="2x" style={{ color: '#f44336', marginRight: '10px' }} />
    <div>
      <p>Unsolved</p>
      <h2>{emails.filter(email => email.status === 'Unsolved').length}</h2>
    </div>
  </div>
</div>
        <div className="email-section">
          <div className="email-header">
            <h2>All Emails</h2>
            <div className="filters">
              <div className="filter-group">
                <input 
                  type="radio" 
                  id="all" 
                  name="status" 
                  checked={filterStatus === 'all'} 
                  onChange={() => handleFilterChange('all')} 
                />
                <label htmlFor="all">All</label>
              </div>
              <div className="filter-group">
                <input 
                  type="radio" 
                  id="active" 
                  name="status" 
                  checked={filterStatus === 'active'} 
                  onChange={() => handleFilterChange('active')} 
                />
                <label htmlFor="active">Active</label>
              </div>
              <div className="filter-group">
                <input 
                  type="radio" 
                  id="inactive" 
                  name="status" 
                  checked={filterStatus === 'inactive'} 
                  onChange={() => handleFilterChange('inactive')} 
                />
                <label htmlFor="inactive">Inactive</label>
              </div>
            </div>
          </div>
          <table className="email-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Email</th>
                <th>Subject</th>
                <th>Priority</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {filteredEmails.map(email => (
                <tr key={email.id}> {/* Assuming `id` is the unique identifier */}
                  <td>{email.id}</td>
                  <td>{email.email}</td>
                  <td>{email.subject}</td>
                  <td>{email.priority}</td>
                  <td>{email.status}</td>
                  <td><button onClick={() => handleViewEmail(email)}>View</button></td>
                </tr>
              ))}
            </tbody>
          </table>
          <div className="pagination">
            <button>Previous</button>
            <button>Next</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
