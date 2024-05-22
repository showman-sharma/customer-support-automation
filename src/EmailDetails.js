import React from 'react';
import { useParams } from 'react-router-dom';
import './EmailDetails.css';

const emails = [
  { id: 123, subject: 'Password Reset', priority: 'High', status: 'UnSolved', content: 'Please reset your password.' },
  { id: 124, subject: 'Subscription Update', priority: 'Medium', status: 'Solved', content: 'Your subscription has been updated.' },
  { id: 125, subject: 'Welcome Email', priority: 'Low', status: 'UnSolved', content: 'Welcome to our service!' },
];

function EmailDetails() {
  const { id } = useParams();
  const email = emails.find(email => email.id === parseInt(id));

  if (!email) {
    return <div>Email not found</div>;
  }

  return (
    <div className="email-details">
      <div className="ticket-id">
        <p>Ticket ID: {email.id}</p>
      </div>
      <div className="customer-details">
        <h3>Customer Details</h3>
        <p>Name: John Doe</p>
        <p>Email: john@example.com</p>
        <p>Phone: (555) 123-4567</p>
      </div>
      <div className="issue-details">
        <h3>Issue Details</h3>
        <p>Summary: {email.subject}</p>
        <p>Description: {email.content}</p>
        <h4>Previous Responses:</h4>
        <p>[2024-05-10] Automated: "We are looking into your issue."</p>
      </div>
      <div className="technician-notes">
        <h3>Technician Notes</h3>
        <button>Add New Note</button>
      </div>
      <div className="response">
        <h3>Response</h3>
        <textarea placeholder="Reply Box"></textarea>
        <div className="response-actions">
          <button>Send</button>
          <button>Save Draft</button>
          <button>Templates</button>
        </div>
      </div>
      <div className="automation-log">
        <h3>Automation Log</h3>
        <p>Attempted Steps:</p>
        <p>Step 1: Reset password (failed)</p>
        <p>Step 2: Check account status (successful)</p>
        <button>Re-run Automation</button>
      </div>
    </div>
  );
}

export default EmailDetails;
