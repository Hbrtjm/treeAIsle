// import { FormEvent, useState, ChangeEvent } from 'react'

import { useState, ChangeEvent, FormEvent } from 'react';

import InputBox from './InputBox.tsx'

interface UserProps {
  username: string;
  email: string;
  password: string;
  repeated_password: string;
}

function Register() {
  const [userCredentials , setUserCredentials] = useState<UserProps>({
    username: '',
    email: '',
    password: '',
    repeated_password: ''
  });

  const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    setUserCredentials({
      ...userCredentials,
      [event.target.name]: event.target.value
    });
  };

  const handleSubmit = async (e : FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const loginData : UserProps = {
      username:userCredentials.username,
      email:userCredentials.email,
      password:userCredentials.password,
      repeated_password:userCredentials.repeated_password,
    };
    try {
      console.log("Connecting to API...");
      const response = await fetch(`/api/register`, {
        method: 'POST',
        headers: {
          'register':'register',
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

  const inputFields = [
    { placeholder: 'Enter your username', name: 'username'  as keyof UserProps },
    { placeholder: 'Enter your email', name: 'email'  as keyof UserProps },
    { placeholder: 'Enter your password', name: 'password' as keyof UserProps , type: 'password' },
    { placeholder: 'Repeat your password', name: 'repeated_password' as keyof UserProps , type: 'password' }
  ];

  return (
    <>
      <div className="login-container">
        <img src="treeAIsle_logo.webp" alt="TreeAIsle" className="logo"></img>
        <h2>Log into your treeAIsle account</h2>
        <form className="login-form" onSubmit={handleSubmit}>
          {inputFields.map((field, index) => (
            <InputBox
              key={index}
              type={field.type}
              name={field.name}
              // A typescript problem, have to define a type of userCredentials, for now it's 'any'
              value={userCredentials[field.name]}
              placeholder={field.placeholder}
              onChange={handleInputChange}
            />
          ))}
          <button type="submit">Register</button>
        </form>
      </div>
    </>
  );
}

export default Register;