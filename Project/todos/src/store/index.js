import { createStore } from 'redux'
import todosReducer from './todos.reducer'
export const store = createStore(todosReducer)
