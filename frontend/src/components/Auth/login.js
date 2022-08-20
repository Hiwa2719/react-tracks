import React from 'react';


const Login = () => {
    return (
        <form>
            <label htmlFor="username" className="d-block text-start">Username</label>
            <input type="text" id="username" className="form-control my-3" placeholder="Username"/>
            <label htmlFor="password" className="d-block text-start">password</label>
            <input type="password" id="Password" className="form-control my-3" placeholder="Password"/>
            <input type="submit" className="btn btn-primary my-3 w-100" value="Login"/>
            <button className="btn btn-outline-warning w-100">New user? Register here</button>
        </form>
    )
}


export default Login