import 'bootstrap/dist/css/bootstrap.css'
import Auth from './components/Auth/auth'
import React, {useEffect, useState} from 'react'


function App() {
    const [loggedIn, setLoggedIn] = useState(()=>{
        return localStorage.getItem('authToken')
    })


  return (
      <div>
          {!loggedIn && <Auth setLoggedIn={setLoggedIn}/>}
      </div>
  );
}

export default App;
