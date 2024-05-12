import React from 'react';
import LoginButton from "./components/LoginButton";
import LogoutButton from "./components/LogoutButton";
import Profile from "./components/Profile";
import { useAuth0 } from "@auth0/auth0-react";
import './styles.css';

function App() {
  const { isLoading, error, user } = useAuth0(); // Define user here
  console.log("Current user", user);

  return (
    <center>
    <main className="column">
      <h1>Login</h1>
      {error && <p>Authentication Error</p>}
      {!error && isLoading && <p>Loading...</p>}
      {!error && !isLoading && (
        <>
          <LoginButton />
          <LogoutButton />
          <Profile />
        </>
      )}
    </main>
    </center>
  );
}

export default App;
