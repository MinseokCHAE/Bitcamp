import React, { useState } from 'react'


const Todo = () => {
    const  [ item, setItem]  = useState('')

    return (<>
    <h1> Todo List </h1>
    <h4> {item} </h4>
    
    <input onChange = { e => setItem(e.target.value) } /> <br/>
    <button onClick = { () => setItem('') }> Delete </button>
    </>)
}

export default Todo