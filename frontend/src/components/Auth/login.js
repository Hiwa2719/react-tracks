import React, {useState} from 'react';
import Lock from "@material-ui/icons/Lock";
import gql from "graphql-tag";
import { useQuery, useMutation } from "@apollo/client";

const LOGIN_QUERY = gql`
    mutation($username: String!, $password: String!){
        tokenAuth(username: $username, password: $password){
            token
        }
    }
`

const Login = ({setLoginScreen, setLoggedIn}) => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [getToken] = useMutation(LOGIN_QUERY, {
        onCompleted: (data)=> {
            localStorage.setItem('authToken', data.tokenAuth.token)
            setLoggedIn(data.tokenAuth.token)
        }
    })

    const submitHandler = (e) => {
        e.preventDefault()
        getToken({
            variables: {
                username: username,
                password: password
            }
        })
    }
    return (
        <form onSubmit={submitHandler}>
            <span className="text-light rounded-circle bg-primary p-2">
                <Lock/>
            </span>
            <h3 className="mt-3">Login as Existing User</h3>
            <label htmlFor="username" className="d-block text-start">Username</label>
            <input type="text" id="username" className="form-control my-3" placeholder="Username"
                   onChange={(e) => setUsername(e.target.value)}/>
            <label htmlFor="password" className="d-block text-start">password</label>
            <input type="password" id="Password" className="form-control my-3" placeholder="Password"
                   onChange={(e) => setPassword(e.target.value)}/>
            <input type="submit" className="btn btn-primary my-3 w-100" value="Login"/>
            <button className="btn btn-outline-warning w-100" onClick={() => setLoginScreen(false)}>
                New user? Register here
            </button>
        </form>
    )
}


export default Login