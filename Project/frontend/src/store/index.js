import { createStore } from 'redux'
import todosReducer from './todos.reducer'
export { default as todosReducer} from './todos.reducer'
export const store = createStore(todosReducer)
