import React from 'react'
import { Route } from "react-router-dom"
import { Counter, Todo, Todos } from 'Components/index'
import { Home } from 'Common/index'


const App = () => {
  return (
  <>
    <Route exact path = '/' component = {Home}/>
    <Route exact path = '/' component = {Counter}/>
    <Route exact path = '/' component = {Todo}/>
    <Route exact path = '/' component = {Todos}/>
    </>
  )
}

export default App