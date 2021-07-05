import React,{useState} from 'react'
import { userLogin } from 'api'
import { useHistory } from 'react-router'

const Login = () => {
    const history = useHistory()
    const [loginRequest, setLoginRequest] = useState({
      userid: '',
      password: ''
    })

    const {userid, password} = `loginRequest`

    
  const handleSubmit = e => {
    e.preventDefault()
    alert(`Click: ${JSON.stringify({...loginRequest})}`)
    userLogin({...loginRequest})
    .then(res => {
      if(JSON.stringify(res.data[0]) === 'FAIL')
      {alert(`Result : ${JSON.stringify(res.data[0])} `)}
        else
        {alert(`Result : ${res.data.result} `)
        localStorage.setItem('loginedUser', JSON.stringify(res.data))
        history.push('/user-list')

      }})
    .catch(err => {
      alert(`Result : ${err} `)

    })
  }


  const handleChange = e => {
    const { name, value } = e.target
    setLoginRequest({
      ...loginRequest,
      [name]: value
    })

  }


    return (<>
      <h2>Login Form</h2>

      <form onSubmit={handleSubmit} method="post" >
          <div className="imgcontainer">
            <img src="https://www.w3schools.com/howto/img_avatar2.png" style={{width: "300px"}} alt="Avatar" className="avatar"/>
          </div>

        <div className="container">
          <label labelFor="userid"><b>ID</b></label>
          <input type="text" placeholder="Enter ID" onChange={handleChange} name="userid" value={userid} required/>

          <label labelFor="password"><b>Password</b></label>
          <input type="password" placeholder="Enter Password" onChange={handleChange} name="password" value={password} required/>
              
          <button type="submit">Login</button>
          <label>
            <input type="checkbox" checked="checked" name="remember"/> Remember me
          </label>
        </div>

        <div className="container" style={{backgroundColor: "#f1f1f1"}}>
          <button type="button" className="cancelbtn">Cancel</button>
          <span className="password">Forgot <a href="#">password?</a></span>
        </div>
      </form>
   
    </>)
}

export default Login