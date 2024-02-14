import { createContext, useState } from 'react';
import Navbar from './Pages/Sources/Navbar.tsx'
import Views from './Views.tsx';
// import UserContext from './User.tsx'
export const UserContext = createContext('user'); 

function App(){
    return (
        /* <UserContext.ProvideContext> */
        <>
            <Navbar />
            <Views/>
        </>  
        /*  */
    )
}

export default App;