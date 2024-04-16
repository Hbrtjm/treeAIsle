import { useState, FormEvent, ChangeEvent } from 'react'
import '../CSS/App.css'
import '../CSS/Login.css'
import { Navigate } from 'react-router-dom';
import { useLocation } from 'react-router'
import InputBox from './InputBox';
import login from '../../Auth.tsx'

interface UserProps {
  username: string;
  password: string;
}

function Login() {
  let notlogged = true;
  const location = useLocation();
  const [wrongPassword, setWrongPassword] = useState(false);
  const [userCredentials, setUserCredentials] = useState<UserProps>({
    username: '',
    password: ''
  });
  function handleWrongPassword() {
    setWrongPassword(true)
  }
  const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    setUserCredentials({
      ...userCredentials,
      [event.target.name]: event.target.value
    });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const loginData: UserProps = {
      username: userCredentials.username,
      password: userCredentials.password
    };

    try {
      console.log("Connecting to API...");
      const response = await fetch(`user_auth/login`, {
        method: 'POST',
        headers: {
          'login': 'login',
          'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(loginData)
      });
      console.log("Got a response!");
      const data = response;
      console.log(data)
      if (data.status == 202) {
        console.log("Redirecting...");
        notlogged = false;
        //window.location.reload();
        console.log(notlogged);
      }
      if (data.status == 404 || data.status == 401) {
        console.log("Wrong password...");
        handleWrongPassword();
      }
    } catch (error) {
      console.log(error);
      //console.error("Cannot connect to API", error);
      alert("Cannot connect to API");
    }
  };

  const inputFields = [
    { placeholder: "Enter your username or email...", name: 'username' as keyof UserProps },
    { placeholder: "Enter your password...", name: 'password' as keyof UserProps, type: 'password' }
  ];

  return notlogged ? (
    <>
      <div className="login-container">
        <img src="treeAIsle_logo.webp" alt="TreeAIsle" className="logo"></img>
        <h2>Log into your treeAIsle account</h2>
        <p>{wrongPassword && "Wrong username or password"}</p>
        <form className="login-form" onSubmit={handleSubmit}>
          {inputFields.map((field, index) => (
            <InputBox
              key={index}
              type={field.type}
              name={field.name}
              // A typescript problem, have to define a type of userCredentials, for now it's 'any', problem with 
              // indexing by a string in
              value={userCredentials[field.name]}
              placeholder={field.placeholder}
              onChange={handleInputChange}
            />
          ))}
          <button type="submit">
            Log in
          </button>
        </form>
      </div>
    </>
  ) : (<Navigate to='/account' replace state={{ from: location }} />);
}

export default Login;
