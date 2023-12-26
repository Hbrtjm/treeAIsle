

function Homepage ()
{
    return (<>
    <ul>
        
        <li>
            <button onClick={ () => window.location.href = "/login" }>Login</button>
        </li>
        
        <li>
            <button onClick={ () => window.location.href = "/register" }>Register</button>
        </li>

    </ul>
    Default Homepage
    
    </>);
} 

export default Homepage;