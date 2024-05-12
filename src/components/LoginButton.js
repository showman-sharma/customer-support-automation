import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';

const LoginButton = () => {
    const { loginWithRedirect, isAuthenticated } = useAuth0();

    const buttonStyle = {
        backgroundColor: '#007bff',
        color: '#fff',
        border: 'none',
        borderRadius: '4px',
        padding: '10px 20px',
        fontSize: '16px',
        cursor: 'pointer',
        transition: 'background-color 0.3s ease',
    };

    const handleClick = () => {
        loginWithRedirect();
    };

    return (
        !isAuthenticated && (
            <button style={buttonStyle} onClick={handleClick}>
                Sign In
            </button>
        )
    );
};

export default LoginButton;
