import React from 'react'
import { Route } from "react-router-dom"
import { Counter } from 'counter/index'
import { Home } from 'common/index'
import { SignUp, Login, UserDetail, UserList, UserEdit } from 'user/index'


const App = () => {
  return (<>
    <Route exact path='/' component={Counter}/>
    <Route exact path='/' component={Home}/>
    <Route exact path='/' component={SignUp}/>
    <Route exact path='/' component={Login}/>
    <Route exact path='/' component={UserDetail}/>
    <Route exact path='/' component={UserList}/>
    <Route exact path='/' component={UserEdit}/>
    </>)
}

export default App