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
  const [showChecklist, setShowChecklist] = useState(true);
  const [userCredentials , setUserCredentials] = useState<UserProps>({
    username: '',
    email: '',
    password: '',
    repeated_password: ''
  });
  const isLongEnough = userCredentials.password.length >= 8;
  const hasLowercase = /[a-z]/.test(userCredentials.password);
  const hasUppercase = /[A-Z]/.test(userCredentials.password);
  const hasSpecialChar = /[;:/?+\-\\_]/.test(userCredentials.password);
  const noWhitespace = !/\s/.test(userCredentials.password);
  const passwordCorrect = isLongEnough && hasLowercase && hasUppercase && hasSpecialChar && noWhitespace;
  // Password checklist handler
  const handleFocus = () => {
      setShowChecklist(true);
  };

  const handleBlur = () => {
      setShowChecklist(false);
  };

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
    if(passwordCorrect)
    {
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
    }
    else
    {
      
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
            field.name != "password" ?
            <InputBox
              key={index}
              type={field.type}
              name={field.name}
              // A typescript problem, have to define a type of userCredentials, for now it's 'any'
              value={userCredentials[field.name]}
              placeholder={field.placeholder}
              onChange={handleInputChange}
            />
            :
            <div>
            <InputBox
              key={index}
              type={field.type}
              name={field.name}
              // A typescript problem, have to define a type of userCredentials, for now it's 'any'
              value={userCredentials[field.name]}
              placeholder={field.placeholder}
              onChange={handleInputChange}
              onBlur={handleBlur}
              onFocus={handleFocus}
            />          
            { showChecklist &&  (
              <ul>
                  <li style={{ color: isLongEnough ? 'green' : 'red' }}>At least 8 characters</li>
                  <li style={{ color: hasLowercase ? 'green' : 'red' }}>Contains lowercase letter(s)</li>
                  <li style={{ color: hasUppercase ? 'green' : 'red' }}>Contains uppercase letter(s)</li>
                  <li style={{ color: hasSpecialChar ? 'green' : 'red' }}>Contains special character(s) (;:/?+\-_)</li>
                  <li style={{ color: noWhitespace ? 'green' : 'red' }}>No whitespace</li>
              </ul>
          ) }
            </div>
          ))}

          <button type="submit">Register</button>
        </form>
      </div>
    </>
  );
}

export default Register;