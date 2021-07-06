import React from 'react'
import { Redirect, Route, Link} from "react-router-dom"
import { Home, User, Item, Board } from 'templates'
import { Login, SignUp, UserDetail, UserEdit, UserList, UserRemove } from 'user'
import { ItemList, ItemRegister, ItemDetail, ItemRemove } from 'item'
import { PostList, PostWrite, PostModify, PostRemove } from 'board'
import { Nav } from 'common'
import { BrowserRouter as Router } from 'react-router-dom'


const App = () => {
  return (<div>
    <Router>
          <Nav/>
          <nav style={{width: '500px', margin:'0 auto'}}>
            <ol>
                <li><Link to='/home'>Home</Link></li>
                <li><Link to='/user'>User</Link></li>
                <li><Link to='/item'>Item</Link></li>
                <li><Link to='/board'>Board</Link></li>
                
            </ol>
        </nav>
          <Route exact path='/home' component={Home}/>
          <Redirect exact from={'/'} to={'/home'}/>

          <Route exact path='/user' component={User}/>
          <Route exact path='/login' component={Login}/>
          <Route exact path='/signup' component={SignUp}/>
          <Route exact path='/user-detail' component={UserDetail}/>
          <Route exact path='/user-edit' component={UserEdit}/>
          <Route exact path='/user-list' component={UserList}/>
          <Route exact path='/user-remove' component={UserRemove}/>

          <Route exact path='/item' component={Item}/>
          <Route exact path='/item-list' component={ItemList}/>
          <Route exact path='/item-register' component={ItemRegister}/>
          <Route exact path='/item-detail' component={ItemDetail}/>
          <Route exact path='/item-remove' component={ItemRemove}/>

          <Route exact path='/board' component={Board}/>
          <Route exact path='/post-list' component={PostList}/>
          <Route exact path='/post-write' component={PostWrite}/>
          <Route exact path='/post-modify' component={PostModify}/>
          <Route exact path='/post-remove' component={PostRemove}/>
         


    </Router>
  </div>)
}

export default App