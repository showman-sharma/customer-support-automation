import React from 'react';
import { Button, Container, Row, Col } from 'react-bootstrap';

import './App.css'; // Import the CSS file

const App = () => {
  const openGoogleCloudConsole = (mail) => {
    // Open Google Cloud Console using the selected mail provider
    if (mail === 'gmail') {
      // Open Google Cloud Console using Gmail
      window.open('https://console.cloud.google.com/', '_blank');
    } else {
      // Handle other mail providers
      alert(`Opening Google Cloud Console using ${mail} mail`);
    }
  };

  return (
    <Container className="container">
      <Row className="justify-content-center align-items-center">
        <Col xs={12} md={6} className="text-center">
          <h1><center>Gmail Access</center></h1>
          <div className="mb-4">
            <Button variant="primary" className="button" onClick={() => openGoogleCloudConsole('gmail')}>
              Sign in with Gmail
            </Button>
          </div>

          {/* Add more mail providers as needed */}
        </Col>
      </Row>
      
      <p>Don't have OAuth credentials? <a href="https://console.developers.google.com/">Visit Google Developer Console</a></p>

    </Container>
  );
};

export default App;
