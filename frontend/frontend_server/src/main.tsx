import React from 'react'
import ReactDOM from 'react-dom/client'
import Login from './Pages/Sources/Login.tsx'
import Homepage from './Pages/Sources/Homepage.tsx'
import './Pages/CSS/login.css'
import { BrowserRouter, Routes , Route } from 'react-router-dom'
import Register from './Pages/Sources/Register.tsx'

ReactDOM.createRoot(document.getElementById('root')!).render(
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
