import React from 'react';
import Gavel from "@material-ui/icons/Gavel";



const Register = ({setLoginScreen}) => {
    return (
        <form>
            <span className="text-light rounded-circle bg-warning p-2">
                <Gavel/>
            </span>
            <h3 className="mt-3">Register</h3>
            <label htmlFor="username" className="d-block text-start">Username</label>
            <input type="text" id="username" className="form-control my-3" placeholder="Username"/>
            <label htmlFor="email" className="d-block text-start">Email</label>
            <input type="text" id="email" className="form-control my-3" placeholder="Email"/>
            <label htmlFor="password" className="d-block text-start">password</label>
            <input type="password" id="Password" className="form-control my-3" placeholder="Password"/>
            <input type="submit" className="btn btn-primary my-3 w-100" value="Register"/>
            <button className="btn btn-outline-warning w-100" onClick={() => setLoginScreen(true)}>
                Already user? Login here
            </button>
        </form>
    )
}


export default Register