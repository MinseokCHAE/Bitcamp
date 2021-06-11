import React from 'react'
import { TodosInput, TodosList } from '../todos/components/index'


const Todos = ({children}) => (<>
    <h1>Todos</h1>
    
            <TodosInput/>
            <TodosList/>
        
    {children}
</>)

export default Todos
