import React from 'react'
import { Link } from 'react-router-dom'

const Nav = () => (
    <>
    <nav style = {{ width: '500px', margin: '0 auto' }}>
        <ol>
            <li><Link to = '/home'>Home</Link></li>
            <li><Link to = '/user'>User</Link></li>
            
        </ol>
    </nav>
    </>
)

export default Nav