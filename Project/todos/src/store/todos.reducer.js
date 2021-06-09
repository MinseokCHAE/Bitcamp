const initialState = { items: [], item: {} }

export const addItemAction = item => { return ({ type: 'ADD_ITEM', payload: item }) }
export const toggleItemAction = itemID => { return ({ type: 'TOGGLE_ITEM', payload: itemID }) }
export const deleteItemAction = itemID => { return ({ type: 'DELETE_ITEM', payload: itemID }) }

const todosReducer = ( state = initialState, action ) => {
    switch(action.type){
        case 'ADD_ITEM': return {...state, items: [...state.items, action.payload]}
        case 'TOGGLE_ITEM': return {...state, items: state.items.map(item => ( item.id === action.payload) ? {...item, complete: !item.complete} : item )}
        case 'DELETE_ITEM': return {...state, items: state.items.filter(item => item.id !== action.payload)}
        default: return state
    }
}

export default todosReducer
