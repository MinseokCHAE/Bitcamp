import React,{useState} from 'react'
import { useHistory } from 'react-router'
import { userEdit } from 'api'

const UserEdit = () => {
      const [changedPassword, setChangedPassword] = useState('')
      const history = useHistory()

      const handleSubmit = e => {
        e.preventDefault()
        const user = JSON.parse(localStorage.getItem("loginedUser"))
        alert(changedPassword)
        user.password = changedPassword
        alert(JSON.stringify(user))
        
        userEdit({user})
        .then(res => {
          alert(`Result : ${res.data.result} `)
          localStorage.setItem("loginedUser", JSON.stringify(user))
          history.push('/user-list')
          
        })
        .catch(err => {
          alert(`Result : ${err} `)
    
        })
      }
  

    return (<>
    <form method="put" onSubmit={handleSubmit} >
            
                <h2 style={{"text-align":"center"}}>User Edit</h2>
        <div className="container">
          <label labelFor="password"><b>New Password</b></label>
          <input type="password" placeholder="Enter New Password" onChange={e => {setChangedPassword(e.target.value)}} name="password" required/>
              
          <button type="submit">Confirm</button>
         
        </div>

      </form>

       
      </>)
}

export default UserEdit