import React from 'react';
import Login from './login'

const Auth = () => {
    return (
        <div className="position-absolute top-0 left-0 w-100 vh-100 overflow-hidden">
            <div className="row justify-content-center mt-5 ">
                <div className="col-6 col-md-4 col-xl-3 p-3 rounded text-center shadow">
                    <Login/>
                </div>
            </div>
        </div>
    )
}


export default Auth