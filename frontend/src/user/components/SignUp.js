import React,{useState} from 'react'
import './SignUp.css'
import { Button } from '@material-ui/core';
import { useHistory } from 'react-router';
import { userSignup } from 'api'


const SignUp = () => {
  const history = useHistory()
  const [userInfo, setUserInfo] = useState({
    userid: '',
    password: '',
    name: '',
    email: ''
  })

  const { userid, password, name, email } = userInfo

  const handleChange = e => {
    const { name, value } = e.target
    setUserInfo({
      ...userInfo, [name]: value
    })
  }
  
  const handleSubmit = e => {
    e.preventDefault()
    userSignup({...userInfo})
    .then(res => { alert(`signup success: ${res.data.result}`) 
    //history.push('login')
  })
    .catch(err => { alert(`signup failed: ${err}`)})
  }

  const handleClick = e => {
    e.preventDefault()
    alert('cancel')
  }

  return (<>
  <div className='Signup'>
    <form onSubmit={handleSubmit} method='post' style={{border:"1px solid #ccc"}}>
  <div className="container">
    <h1>Sign Up</h1>
    <p>Please fill in this form to create an account.</p>
    <hr/>

    <label for="userid"><b>ID</b></label>
    <input type="text" placeholder="Enter ID" onChange={handleChange} name="userid" value={userid}/>

    <label for="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" onChange={handleChange} name="password" value={password}/>

    <label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter Name" onChange={handleChange} name="name" value={name}/>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" onChange={handleChange} name="email" value={email}/>

    <p>By creating an account you agree to our <a href="#" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>

    <div class="clearfix">
      <button type="submit" className="signupbtn">Sign Up</button>
      <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
    </div>
  </div>
  
</form>
</div>
</>)
}

export default SignUp
