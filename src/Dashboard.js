import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTachometerAlt, faBox, faUsers, faDollarSign, faBullhorn, faQuestionCircle } from '@fortawesome/free-solid-svg-icons';
import './App.css';
import './Dashboard.css';

const initialEmails = [
  { id: 123, subject: 'Password Reset', priority: 'Inactive', status: 'UnSolved', content: 'Please reset your password.' },
  { id: 124, subject: 'Subscription Update', priority: 'Active', status: 'Solved', content: 'Your subscription has been updated.' },
  { id: 125, subject: 'Welcome Email', priority: 'Inactive', status: 'UnSolved', content: 'Welcome to our service!' },
];

function Dashboard() {
  const [searchTerm, setSearchTerm] = useState('');
  const [emails, setEmails] = useState(initialEmails);
  const [filterStatus, setFilterStatus] = useState('all'); // 'all', 'active', 'inactive'
  const navigate = useNavigate();

  const filteredEmails = emails.filter(email => {
    const matchesSearchTerm = email.subject.toLowerCase().includes(searchTerm.toLowerCase());
    if (filterStatus === 'active') {
      return email.status === 'Solved';
    } else if (filterStatus === 'inactive') {
      return email.status === 'UnSolved';
    }
    return matchesSearchTerm;
  });

  const handleViewEmail = (email) => {
    navigate(`/email/${email.id}`);
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
        <h1>Customer Details Dashboard</h1>
        <div className="search-bar">
          <input 
            type="text" 
            placeholder="Search for emails..." 
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
        <div className="filter-section">
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
        <table className="email-table">
          <thead>
            <tr>
              <th>Email ID</th>
              <th>Subject</th>
              <th>Priority</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {filteredEmails.map(email => (
              <tr key={email.id}>
                <td>{email.id}</td>
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
  );
}

export default Dashboard;
