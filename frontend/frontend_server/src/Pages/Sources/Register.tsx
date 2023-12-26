import { FormEvent, useState } from 'react'

interface InputBoxProps {
  name: string;
  onChange: Function;
}

function InputBox(InputBoxProp: InputBoxProps) {
  const [inputValue, setInputValue] = useState('');

  const handleValueChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
    InputBoxProp.onChange();
  };
  return (
    <input
      type="text"
      placeholder={`Enter your ${InputBoxProp.name}...`}
      value={inputValue}
      onChange={handleValueChange}
    />
  );
}

interface userProps
{
  username: string;
  email: string;
  password: string;
  repeated_password: string;
}

function Register() {
  const [userCredentials, setUserCredentials] = useState({
    username: '',
    password: '',
    email: '',
    repeated_password:''
  });

  const handleUsernameChange = (updateUsername : React.ChangeEvent<HTMLInputElement>) => {
    setUserCredentials({
      ...userCredentials,
      username: updateUsername.target.value
    });
  };

  const handleEmailChange = (updateEmail : React.ChangeEvent<HTMLInputElement>) => {
    setUserCredentials({
      ...userCredentials,
      email: updateEmail.target.value
    });
  };
  
  const handlePasswordChange = (updatePassword : React.ChangeEvent<HTMLInputElement>) => {
    setUserCredentials({
      ...userCredentials,
      password: updatePassword.target.value
    });
  };
  
  const handleRepeatedPasswordChange = (updateRepeatedPassword : React.ChangeEvent<HTMLInputElement>) => {
    setUserCredentials({
      ...userCredentials,
      repeated_password: updateRepeatedPassword.target.value
    });
  };

  const handleSubmit = async (e : FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const loginData : userProps = {
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

  return (
    <>
    <div className="login-container">
      <img src="treeAIsle_logo.webp" alt="TreeAIsle" className="logo"></img>
        <h2>Log into your treeAIsle account</h2>
        <form className="login-form" onSubmit={handleSubmit}>
          <input
            type="text"
            className="input-box"
            placeholder="Enter your username..."
            value={userCredentials.username}
            onChange={handleUsernameChange}
          />
          <input
            type="text"
            className="input-box"
            placeholder="Enter your email..."
            value={userCredentials.email}
            onChange={handleEmailChange}
          />
          <input
            type="password"
            className="input-box"
            placeholder="Enter your password..."
            value={userCredentials.password}
            onChange={handlePasswordChange}
          />
          <input
            type="password"
            className="input-box"
            placeholder="Repeat your password..."
            value={userCredentials.repeated_password}
            onChange={handleRepeatedPasswordChange}
          />
          <button type="submit">
            Register
          </button>
        </form>
      </div>
    </>
  );
}

// function Register() {
//   const [userCredentials, setUserCredentials] = useState({
//     username: '',
//     email: '',
//     password: '',
//     repeatedPassword: ''
//   });
  
//   const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
//     e.preventDefault();
//     // Access form data from state
//     console.log(userCredentials);
//     // Here, you can perform actions with userCredentials, like API calls or validations
//   };

//   const handleInputChange = (fieldName: string, value: string) => {
//     setUserCredentials((prevCredentials) => ({
//       ...prevCredentials,
//       [fieldName]: value
//     }));
//   };
  

  


//   // InputBox-es are substitutions for copying and pasting the same code 
  
//   return (
//     <div className="login-container">
//       <h2>Register for treeAIsle</h2>
//       <form onSubmit={handleSubmit}>
//         <InputBox name="username" onChange={(value : string) => { handleInputChange('username', value); console.log(value); } } />
//         <InputBox name="email" onChange={(value : string) => handleInputChange('email', value)} />
//         <InputBox name="password" onChange={(value : string) => handleInputChange('password', value)} />
//         <InputBox name="repeated password" onChange={(value : string) => handleInputChange('repeatedPassword', value)} />
//         <button type="submit">Register</button>
//       </form>
//     </div>
//   );
// }

export default Register;