// EmailDetails.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import './EmailDetails.css'; // Import your CSS file

function EmailDetails() {
  const { id } = useParams(); // Assuming your API uses `id` as the identifier
  const [emailDetails, setEmailDetails] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchEmailDetails = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/emails/${id}`);
        setEmailDetails(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching email details:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchEmailDetails();
  }, [id]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!emailDetails) {
    return <div>No email details found.</div>;
  }

  return (
    <div className="email-details">
      <h2>User Details</h2>
      <div className="email-details-item">
        <strong>Email ID:</strong> <span>{emailDetails.id}</span>
      </div>
      <div className="email-details-item">
        <strong>Email:</strong> <span>{emailDetails.email}</span>
      </div>
      <div className="email-details-item">
        <strong>Subject:</strong> <span>{emailDetails.subject}</span>
      </div>
      <div className="email-details-item">
        <strong>Priority:</strong> <span>{emailDetails.priority}</span>
      </div>
      <div className="email-details-item">
        <strong>Status:</strong> <span>{emailDetails.status}</span>
      </div>
      {/* Additional details as needed */}
    </div>
  );
}

export default EmailDetails;
