import { FormEventHandler, useState } from 'react'
import './App.css'

interface userProps {
  username : string,
  password : string
}

function Login() {
  const [count, setCount] = useState(0);
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

  const handlePasswordChange = (event : React.ChangeEvent<HTMLInputElement>) => {
    setUserCredentials({
      ...userCredentials,
      password: event.target.value
    });
  };

  const handleSubmit = async () => {
    try {
      console.log("Connecting to API...");
      const response = await fetch(`https://http://127.0.0.1:8000/aileapp/api/login/username=${userCredentials.username}&password=${userCredentials.password}`, {
        method: 'GET',
      });
      console.log("Got a response!");
      const data = await response.json();
      console.log("API request received!", data);
    } catch (error) {
      console.error("Cannot connect to API", error);
      alert("Cannot connect to API");
    }
  };

  return (
    <>
      <div className="card">
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
          <button type="submit" onClick={() => setCount((count) => count + 1)}>
            Count is {count}
          </button>
        </form>
      </div>
    </>
  );
}

export default Login;
