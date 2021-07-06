import React,{useEffect, useState} from 'react'
import { userRemove } from 'api'
import { useHistory } from 'react-router'

const UserRemove = () => {
    const [deletedPassword, setDeletedPassword] = useState('')
    const history = useHistory()
    const handleSubmit = e => {
      e.preventDefault()
      const user = JSON.parse(localStorage.getItem("loginedUser"))
      if(deletedPassword === user.password){
        userRemove(user.userid)
        .then(res => {
        alert(`Result : ${res.data.result} `)
        localStorage.setItem("loginedUser", "")
        history.push('/home')
        
        })
        .catch(err => {
        alert(`Remove Failed : ${err} `)
  
        })
      }else{
        alert('Incorrect Password')
        document.getElementById("password").value = ""
      }
      
    }

    return (<>
    <form method="delete" onSubmit={handleSubmit} >
          <h2 style={{"text-align":"center"}}>User Remove</h2>
          <div className="container">
          <label labelFor="password"><b>Password </b></label>
          <input type="password" id="password" placeholder="Enter Password" onChange={e => {setDeletedPassword(e.target.value)}} name="password" required/>
          <button type="submit">Confirm</button>
        </div>
      </form>
    </>)
}

export default UserRemove