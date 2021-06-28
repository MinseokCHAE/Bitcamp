import React, {useEffect, useState} from 'react'
import axios from 'axios';
import { Button } from '@material-ui/core';


const Home = ({children}) => {
   
    const [ connection, setConnection ] = useState(false)
    const handleClick = e => {
        e.preventDefault()
        axios({
            method: "get",
            url: "http://127.0.0.1:8000/connection",
            responseType: "json"
        }).then(function (res) {
            setConnection(res.data.connection === 'success')
        });
    }
    
    return (<>
    <table className="tab_lay">
        <tr><td><h1>HOME</h1></td></tr>
        <tr><td><Button color='primary' onClick={handleClick}>Server Connection Test</Button></td></tr>
        <tr><td> { connection ? 
        'connection success'
        : 
        'connection failed'
        } </td></tr>
    </table>
    {children}

</>)}


export default Home
