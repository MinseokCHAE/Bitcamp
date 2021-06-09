import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { toggleItemAction, deleteItemAction } from '../store/todos.reducer'


const TodosList = () => {
    const items = useSelector( state => state.items )
    const dispatch = useDispatch()
    const toggleItem = id => dispatch(toggleItemAction(id))
    const deleteItem = id => dispatch(deleteItemAction(id))
    
    return(
        <>
        { items.length === 0 && ( <p className = 'alert alert-info'> no list </p> )}
        { items.length !== 0 && items.map( item => (
            <div key = {item.id} className = 'row mb-1'>
            <div className = 'col-sm-2'> 
            <input type = 'checkbox' checked = {item.complete} onChange = {toggleItem.bind(null, item.id)} />
            { item.complete 
            ? <span style = {{ textDecoration: 'line-through' }} > {item.name} </span>
            : <span> {item.name} </span> }
            <button onClick = { deleteItem.bind(null, item.id) }> remove </button>
            </div>
            </div>))}
        </>
    )
}

export default TodosList