import React from 'react';

class GmailAccess extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      accessToken: null
    };
  }

  componentDidMount() {
    // Load the Google API client asynchronously
    const script = document.createElement('script');
    script.src = 'https://apis.google.com/js/api.js';
    script.onload = this.initClient;
    document.body.appendChild(script);
  }

  initClient = () => {
    window.gapi.load('client:auth2', this.initAuthClient);
  };

  initAuthClient = () => {
    window.gapi.client
      .init({
        clientId: '992977703333-eba3to9jruvv9naluhr2upipmc4qc36f.apps.googleusercontent.com',
        scope: 'https://www.googleapis.com/auth/gmail.readonly',
        discoveryDocs: ['https://www.googleapis.com/discovery/v1/apis/gmail/v1/rest']
      })
      .then(() => {
        // Listen for sign-in state changes.
        window.gapi.auth2.getAuthInstance().isSignedIn.listen(this.updateSignInStatus);
        // Handle the initial sign-in state.
        this.updateSignInStatus(window.gapi.auth2.getAuthInstance().isSignedIn.get());
      })
      .catch(error => {
        console.error('Error initializing Google API client: ', error);
      });
  };

  updateSignInStatus = isSignedIn => {
    if (isSignedIn) {
      const currentUser = window.gapi.auth2.getAuthInstance().currentUser.get();
      const accessToken = currentUser.getAuthResponse().access_token;
      this.setState({ accessToken });
    } else {
      this.setState({ accessToken: null });
    }
  };

  handleSignInClick = () => {
    window.gapi.auth2.getAuthInstance().signIn()
      .then(() => {
        // Sign-in successful, handle any further actions if needed
        console.log('Sign-in successful');
      })
      .catch(error => {
        // Handle sign-in errors
        console.error('Error signing in:', error);
      });
  };

  handleSignOutClick = () => {
    window.gapi.auth2.getAuthInstance().signOut();
  };

  render() {
    const { accessToken } = this.state;

    return (
      <div style={{ maxWidth: '400px', margin: '0 auto', padding: '20px', backgroundColor: '#f9f9f9', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)' }}>
        <div style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '20px' }}>Gmail Access</div>
        {accessToken ? (
          <div>
            <p>Access token: {accessToken}</p>
            <button style={{ display: 'block', width: '100%', padding: '12px 20px', fontSize: '16px', fontWeight: 'bold', color: '#fff', backgroundColor: '#4285f4', border: 'none', borderRadius: '4px', cursor: 'pointer', transition: 'background-color 0.3s ease' }} onClick={this.handleSignOutClick}>Sign out</button>
          </div>
        ) : (
          <div>
            <button style={{ display: 'block', width: '100%', padding: '12px 20px', fontSize: '16px', fontWeight: 'bold', color: '#fff', backgroundColor: '#4285f4', border: 'none', borderRadius: '4px', cursor: 'pointer', transition: 'background-color 0.3s ease' }} onClick={this.handleSignInClick}>Sign in with Google</button>
            <div style={{ marginTop: '20px' }}>
              <p>Don't have OAuth credentials? <a style={{ color: '#4285f4', textDecoration: 'none' }} href="https://console.developers.google.com/">Visit Google Developer Console</a></p>
            </div>
          </div>
        )}
      </div>
    );
  }
}

export default GmailAccess;
