import { useContext } from "react";
import { useLocation } from "react-router"
import { Navigate , Outlet } from "react-router-dom";
import { UserContext } from "./App.tsx";

const useAuth = () => {
    const { user } = useContext(UserContext);
    return user && user.loggedIn;
}

const ProtectedRoutes = () => {
    const location = useLocation();
    const isAuth = useAuth();
    console.log(isAuth);
    return isAuth ? 
    (
        <Outlet />
    ) :
    (
        <Navigate to='/login' replace state={{from:location}} />
    );
}

export default ProtectedRoutes;
