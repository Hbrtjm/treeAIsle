import { Navigate , Outlet } from "react-router-dom";

const useAuth = () => { 
    const user = { loggedIn: false };
    return user && user.loggedIn;
};

const ProtectedRoutes = () => {
    console.log("f");
    const isAuth = useAuth();
    return isAuth ? <Outlet /> : <Navigate to='/login' />;
};

export default ProtectedRoutes;
