import React from 'react';
import Lock from "@material-ui/icons/Lock";


const Login = ({setLoginScreen}) => {
    return (
        <form>
            <span className="text-light rounded-circle bg-primary p-2">
                <Lock />
            </span>
            <h3 className="mt-3">Login as Existing User</h3>
            <label htmlFor="username" className="d-block text-start">Username</label>
            <input type="text" id="username" className="form-control my-3" placeholder="Username"/>
            <label htmlFor="password" className="d-block text-start">password</label>
            <input type="password" id="Password" className="form-control my-3" placeholder="Password"/>
            <input type="submit" className="btn btn-primary my-3 w-100" value="Login"/>
            <button className="btn btn-outline-warning w-100" onClick={() => setLoginScreen(false)}>
                New user? Register here
            </button>
        </form>
    )
}


export default Login