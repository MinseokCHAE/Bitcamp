import React from 'react'


const Home = ({children}) => (<>
    <table className="tab_lay">
        <tr><td><h1>HOME</h1></td></tr>
        <tr><td><button >Server Connection Test</button></td></tr>
    </table>
    {children}

</>)


export default Home


export const Counter = () => {
    return (<></>)
}