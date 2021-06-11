import React, { useState } from 'react'
import { v4 as uuidv4 } from 'uuid'
import { useDispatch } from 'react-redux'
import { addItemAction } from '../../store/todos.reducer'


const TodosInput = () => {
    const [ item, setItem ] = useState('')
    const dispatch = useDispatch()
    
    const submitForm = e => {
        e.preventDefault()
        console.log( `uuidv4 : ${ uuidv4() }` )

        const newItem = {
            id: uuidv4(),
            name: item,
            complete: false
        }
        addItem(newItem)
        setItem('')
    }
    const addItem = item => dispatch(addItemAction(item))    

    const handleChange = e => {
        e.preventDefault()
        setItem(e.target.value)
    }

    return(
        <>
        <h1> Todos </h1>
        <h4> {item} </h4>
        <form onSubmit = { submitForm } method = 'POST' > 
            <div className = 'row mt-3'>
                <div className = 'form-group col-sm-8'>
                    <input
                    type = 'text'
                    placeholder = 'input item'
                    name = 'item'
                    className = 'form-control'
                    value = {item}
                    onChange = { handleChange } />
                </div>
            </div>
        </form>
        </>
    )
}

export default TodosInput