import React from 'react';

class HomePage extends React.Component {
  handleCloudConsoleRedirect = () => {
    window.location.href = 'https://console.cloud.google.com/welcome?project=myproject3-420810';
  }

  handleFormRedirect = () => {
    // Navigate to the Form component
    this.props.history.push('/form');
  }

  render() {
    return (
      <div style={{ backgroundColor: '#f0f0f0', padding: '20px' }}>
        <div style={{ textAlign: 'center', margin: '20px 0' }}>
          <button onClick={this.handleCloudConsoleRedirect} style={{ backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: '4px', padding: '10px 20px', cursor: 'pointer' }}>Go to Cloud Console</button>
        </div>
        <div style={{ textAlign: 'center', margin: '20px 0' }}>
          <h2 style={{ color: '#333' }}>Instructions:</h2>
          <p style={{ color: '#555' }}>1. Follow the link above to access the Cloud Console.</p>
          <p style={{ color: '#555' }}>2. Complete the necessary tasks in the console.</p>
          <p style={{ color: '#555' }}>3. Once done, click the button below to proceed to the credentials form.</p>
        </div>
        <div style={{ textAlign: 'center', margin: '20px 0' }}>
          <button onClick={this.handleFormRedirect} style={{ backgroundColor: '#28a745', color: '#fff', border: 'none', borderRadius: '4px', padding: '10px 20px', cursor: 'pointer' }}>Go to Form</button>
        </div>
      </div>
    );
  }
}

export default HomePage;
