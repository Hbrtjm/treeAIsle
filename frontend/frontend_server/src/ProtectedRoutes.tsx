import { Navigate , Outlet } from "react-router-dom";
const useAuth = () => {
    console.log("F");
    const user = { loggedIn: false };
    return user && user.loggedIn;
};

const ProtectedRoutes = () => {
    const isAuth = useAuth();
    return isAuth ? <Outlet />:<Navigate to='/login' />;
};

export default ProtectedRoutes;
