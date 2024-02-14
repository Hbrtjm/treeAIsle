import { Navigate , Outlet } from "react-router-dom";
const useAuth = () => {
    const user = { loggedIn: false };
    return user && user.loggedIn;
}

const ProtectedRoutes = () => {
    const isAuth = useAuth();
    console.log(isAuth);
    return isAuth ? 
    (
        <Outlet />
    ) :
    (
        <Navigate to='/login' />
    );
}

export default ProtectedRoutes;
