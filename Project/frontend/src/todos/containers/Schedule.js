import React from 'react'
import { TodosInput, TodosList } from '../Test/index'
import { Provider } from 'react-redux'
import { store } from '../store/index'


const Schedule = () => {
    return (
        <>
        <Provider store = { store } >
            <TodosInput/>
            <TodosList/>
        </Provider>
        </>
    )
}

export default Schedule