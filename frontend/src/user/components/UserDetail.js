import React, { useEffect, useState } from 'react'


const UserDetail = () => {
  const [member, setUser] = useState({})

  useEffect(() => {
    setUser(JSON.parse(localStorage.getItem("selectedUser")))
  }, {})
    return (<>
  <div className="user-detail-card">
                <h2 style={{"text-align":"center"}}>User Detail</h2>
                <img src="https://www.w3schools.com/w3images/team2.jpg"  style={{"width":"100%"}}/>
                <h1>{member.name}</h1>
                    <p className="user-detail-title">CEO & Founder, Example</p>
                    <p>Harvard University</p>
                    <div style={{"margin": "24px 0"}}>
                      <a className="user-detail-a" href="#"><i className="fa fa-dribbble"></i></a> 
                      <a className="user-detail-a" href="#"><i className="fa fa-twitter"></i></a>  
                      <a className="user-detail-a" href="#"><i className="fa fa-linkedin"></i></a>  
                      <a className="user-detail-a" href="#"><i className="fa fa-facebook"></i></a> 
                    </div>
                    <p><button className="user-detail-button">Contact</button></p>
                </div>
  </> )
  }

export default UserDetail