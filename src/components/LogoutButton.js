import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';

const LogoutButton = () => {
    const { logout, isAuthenticated } = useAuth0();

    const buttonStyle = {
        backgroundColor: '#dc3545',
        color: '#fff',
        border: 'none',
        borderRadius: '4px',
        padding: '10px 20px',
        fontSize: '16px',
        cursor: 'pointer',
        transition: 'background-color 0.3s ease',
    };

    const handleClick = () => {
        logout();
    };

    return (
        isAuthenticated && (
            <button style={buttonStyle} onClick={handleClick}>
                Sign Out
            </button>
        )
    );
};

export default LogoutButton;
