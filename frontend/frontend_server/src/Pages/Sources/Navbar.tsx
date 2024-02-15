import '../CSS/Navbar.css'

function Navbar(){
    return (
        <nav> 
            <ul>
                
                <li>
                    <button onClick={ () => window.location.href = "/login" }>Login</button>
                </li>
                
                <li>
                    <button onClick={ () => window.location.href = "/register" }>Register</button>
                </li>
                <li>
                    <button onClick={ () => window.location.href = "/account" }>Account</button>
                </li>
            </ul>
        </nav>
    )
}

export default Navbar;