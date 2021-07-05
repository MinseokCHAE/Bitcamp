import axios from "axios";


const SERVER = 'http://127.0.0.1:8000/'
const headers = {'Content-Type': 'application/json'}

export const userSignup = body => axios.post(`${SERVER}api/member/signup`, {headers, body})
export const userList = () => axios.get(`${SERVER}adm/member/list`)
export const userLogin = body => axios.post(`${SERVER}api/member/login`,{headers, body})
export const boardPostWrite = body => axios.post(`${SERVER}board/postwrite`, {headers, body})

