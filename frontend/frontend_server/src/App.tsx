// import { createContext, useState } from 'react';
import Navbar from './Pages/Sources/Navbar.tsx'
import Views from './Views.tsx';
/*interface User {
    name: string;
    isLoggedIn:Boolean;
}

export const UserContext = createContext<User | undefined>(undefined); 

const [user] = useState({
    name:'',
    isLoggedIn:false
})
*/
function App(){
    return (
        //<UserContext.Provider value={user}>
        <>
            <Navbar />
            <Views />
        </>
        //</UserContext.Provider>
    )
}

export default App;