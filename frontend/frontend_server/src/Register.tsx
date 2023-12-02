import { useState,useEffect } from 'react'

function Register () {
        const [repeatedPassword,setRepeatedPassword] = useState('')
        const [userCredentials, setUserCredentials] = useState({
            username: '',
            email: '',
            password: ''
          });
          const handleRepeatedPasswordChange = (updateRepeatedPassword : React.ChangeEvent<HTMLInputElement>) => {
            setRepeatedPassword(
                updateRepeatedPassword.target.value
            );
          };
          const handleUsernameChange = (updateUsername : React.ChangeEvent<HTMLInputElement>) => {
            setUserCredentials({
              ...userCredentials,
              username: updateUsername.target.value
            });
          };

          const handleEmailChange = (updateUsername : React.ChangeEvent<HTMLInputElement>) => {
            setUserCredentials({
              ...userCredentials,
              username: updateUsername.target.value
            });
          };
        
          const handlePasswordChange = (updatePassword : React.ChangeEvent<HTMLInputElement>) => {
            setUserCredentials({
              ...userCredentials,
              password: updatePassword.target.value
            });
          };
          const handleSubmit = async () => {
            
            return 0;
          }
    return (
        <>
        <div className="login-container">
          <img src="treeAIsle_logo.webp" alt="TreeAIsle" className="logo"></img>
            <h2>Log into your treeAIsle account</h2>
            <form onSubmit={handleSubmit}>
              <input
                type="text"
                placeholder="Enter your username..."
                value={userCredentials.email}
                onChange={handleEmailChange}
              />
              <input
                type="text"
                placeholder="Enter your email..."
                value={userCredentials.username}
                onChange={handleUsernameChange}
              />
              <input
                type="password"
                placeholder="Enter your password"
                value={userCredentials.password}
                onChange={handlePasswordChange}
              />
              <input
                type="password"
                placeholder="Repeat your password"
                value={userCredentials.password}
                onChange={handleRepeatedPasswordChange}
              />
              <button type="submit">
                Log in
              </button>
            </form>
          </div>
        </>
      );
} 

export default Register;