
import React from 'react';
import ReactDOM from 'react-dom';
import { Auth0Provider } from '@auth0/auth0-react';
import App from './App';

ReactDOM.render(
  <Auth0Provider
    domain="dev-8vw4yzjsbr4trcc8.us.auth0.com"
    clientId="9tCZGgKiU6M0RIltuYH9ZSeieLfkoaTp"
    redirectUri={window.location.origin}
  >
    <App />
  </Auth0Provider>,
  document.getElementById('root')
);
