import React from 'react'
import { Route } from "react-router-dom"
import { Counter } from './counter/index'
import { Home } from './common/index'
import { SignUp, Login, UserDetail, UserList, UserEdit } from './user/index'


const App = () => {
  return (
  <div>
    <Route exact path='/Counter' component={Counter}/>
    <Route exact path='/Home' component={Home}/>
    <Route exact path='/SignUp' component={SignUp}/>
    <Route exact path='/Login' component={Login}/>
    <Route exact path='/UserDetail' component={UserDetail}/>
    <Route exact path='/UserList' component={UserList}/>
    <Route exact path='/UserEdit' component={UserEdit}/>
    </div>)
}
export default App