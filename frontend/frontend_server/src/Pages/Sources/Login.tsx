import { useState } from 'react'
import '../CSS/App.css'
import '../CSS/login.css'
import { FormEvent } from 'react';
import { Navigate } from 'react-router-dom';
import { useLocation } from 'react-router'

interface userProps
{
  username: string;
  password: string;
}

function Login() {
  let password_username_error:Boolean = false;
  let notlogged = true;
  const location = useLocation();
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
          'login':'login',
          'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(loginData)
      });
      console.log("Got a response!");
      const data = response;
      // console.log("API request received!", data);
      console.log(data)
      if(data.status==202)
      {
        password_username_error = false;
        console.log("Redirecting...");
        // Can't work like this - the function does not render again
        notlogged = false;
        window.location.reload();
        console.log(notlogged);
      }
      if(data.status==404)
      {
        console.log("Wrong password...");
        password_username_error = true;
      }
    } catch (error) {
      console.log(error);
      //console.error("Cannot connect to API", error);
      alert("Cannot connect to API");
    }
  };
  return notlogged ? (
    <>
    <div className="login-container">
      <img src="treeAIsle_logo.webp" alt="TreeAIsle" className="logo"></img>
        <h2>Log into your treeAIsle account</h2>
        <p>{ password_username_error && "Wrong username or password" }</p>
        <form className="login-form" onSubmit={handleSubmit}>
          <input
            type="text"
            className="input-box"
            placeholder="Enter your username or email..."
            value={userCredentials.username}
            onChange={handleUsernameChange}
          />
          <input
            type="password"
            className="input-box"
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
  ) : (<Navigate to='/account' replace state={{from:location}} />);
}

export default Login;
