import axios from "axios";


const SERVER = 'http://127.0.0.1:8000/'
const headers = {'Content-Type': 'application/json'}

export const userSignup = body => axios.post(`${SERVER}member/signup`, {headers, body})
export const boardPostWrite = body => axios.post(`${SERVER}board/postwrite`, {headers, body})

