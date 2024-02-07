import { createContext, useState } from 'react';
import Navbar from './Pages/Sources/Navbar.tsx'
import Views from './Views.tsx';
export const UserContext = createContext('user'); 

function App(){
    const [user, setUser] = useState({loggedIn:false})
    return (
        <UserContext.Provider value={{user,setUser}}>
            <Navbar />
            <Views/>
        </UserContext.Provider>
    )
}

export default App;