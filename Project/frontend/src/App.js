import React from 'react'
import { Redirect, Route } from "react-router-dom"
import { Home, User, Item, Todos } from 'templates/index'
import { Login, SignUp, UserDetail, UserEdit, UserList } from 'user'
import { ItemDetail, ItemList, ItemRegister, ItemRemove } from 'item'
import { TodosInput, TodosList } from './todos/components'
import { Nav } from 'common'
import { BrowserRouter as Router } from 'react-router-dom'
import { todosReducer } from './store/index'
import { createStore, combineReducers} from 'redux'
import { Provider } from 'react-redux'
const rootReducer = combineReducers({todosReducer})

const App = () => {
  return (<div>
    <Router>
      <Provider store = {createStore(rootReducer)}>1
        <Nav/>
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>

        <Route exact path='/user' component={User}/>
        <Route exact path='/login' component={Login}/>
        <Route exact path='/signup' component={SignUp}/>
        <Route exact path='/user-detail' component={UserDetail}/>
        <Route exact path='/user-edit' component={UserEdit}/>
        <Route exact path='/user-list' component={UserList}/>

        <Route exact path='/item' component={Item}/>
        <Route exact path='/item-list' component={ItemList}/>
        <Route exact path='/item-register' component={ItemRegister}/>
        <Route exact path='/item-detail' component={ItemDetail}/>
        <Route exact path='/item-remove' component={ItemRemove}/>

        <Route exact path='/todos' component={Todos}/>
        


      </Provider>
    </Router>
  </div>)
}

export default App