import React from 'react';
import ReactDOM from 'react-dom/client';
import './Pages/CSS/login.css';
import { BrowserRouter } from 'react-router-dom';
import App from './App.tsx'


ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);