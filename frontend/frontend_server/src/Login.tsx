import { useState } from 'react'
import './App.css'
import { FormEvent } from 'react';

interface userProps
{
  username: string;
  password: string;
}

function Login() {
  const [userCredentials, setUserCredentials] = useState({
    username: '',
    password: ''
  });

  const handleUsernameChange = (event : React.ChangeEvent<HTMLInputElement>) => {
    setUserCredentials({
      ...userCredentials,
      username: event.target.value
    });
  };

  const handlePasswordChange = (updatePassword : React.ChangeEvent<HTMLInputElement>) => {
    setUserCredentials({
      ...userCredentials,
      password: updatePassword.target.value
    });
  };

  const handleSubmit = async (e : FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const loginData : userProps = {
      username:userCredentials.username,
      password:userCredentials.password
    };
    try {
      console.log("Connecting to API...");
      const response = await fetch(`/api/login`, {
        method: 'POST',
        headers: {
          'lgoin':'login',
          'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(loginData)
      });
      console.log("Got a response!");
      const data = response;
      // console.log("API request received!", data);
      console.log(data)
    } catch (error) {
      console.log(error);
      //console.error("Cannot connect to API", error);
      alert("Cannot connect to API");
    }
  };

  return (
    <>
    <div className="login-container">
      <img src="treeAIsle_logo.webp" alt="TreeAIsle" className="logo"></img>
        <h2>Log into your treeAIsle account</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Enter your username or email..."
            value={userCredentials.username}
            onChange={handleUsernameChange}
          />
          <input
            type="password"
            placeholder="Enter your password"
            value={userCredentials.password}
            onChange={handlePasswordChange}
          />
          <button type="submit">
            Log in
          </button>
        </form>
      </div>
    </>
  );
}

export default Login;
