import React, { useState } from 'react';
import './Style.css';

export default function Form() {
    const [email, setEmail] = useState("");
    const [client_id, setClient_id] = useState("");
    const [client_secret, setClient_secret] = useState("");

    const collectData = async (e) => {
        e.preventDefault();
        try {
            let result = await fetch('http://localhost:4000/', {
                method: 'post',
                body: JSON.stringify({ email, client_id, client_secret }),
                headers: {
                    'Content-Type': 'application/json'
                },
            });
            result = await result.json();
            console.log(result);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className='container'>
            <form onSubmit={collectData}>
                <h1 className='text-center pt-3'> CREDENTIALS FORM</h1>
                <div className='mb-3 mt-2'>
                    <label className='form-label'>Email</label>
                    <input type="email" className='form-control'
                        value={email}
                        onChange={(e) => setEmail(e.target.value)} />
                </div>
                <div className='mb-3'>
                    <label className='form-label'>Client_id</label>
                    <input type="text" className='form-control'
                        value={client_id}
                        onChange={(e) => setClient_id(e.target.value)} />
                </div>
                <div className='mb-3'>
                    <label className='form-label'>Client_secret</label>
                    <input type="password" className='form-control'
                        value={client_secret}
                        onChange={(e) => setClient_secret(e.target.value)} />
                </div>
                <button type="submit" className='btn btn-success'>Submit</button>
            </form>
        </div>
    );
}