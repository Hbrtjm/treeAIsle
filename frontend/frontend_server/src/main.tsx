import React from 'react';
import ReactDOM from 'react-dom/client';
import './Pages/CSS/login.css';
import { BrowserRouter } from 'react-router-dom';
import App from './App.tsx'
//import Homepage from './Pages/Sources/Homepage.tsx';
//import Login from './Pages/Sources/Login.tsx';
//import Register from './Pages/Sources/Register.tsx';


/*ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
          <Route path="login" element = { <Login /> } />
          <Route path="/" element={ <Homepage/> }/>
          <Route path="register" element={ <Register/> }/>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
)
*/

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);