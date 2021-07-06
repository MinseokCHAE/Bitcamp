import React from 'react';
import { Link } from 'react-router-dom';
import { useHistory } from 'react-router'

export const UserMenu = () => {  
    const history = useHistory()
    return(
    <nav style = {{ width: '500px', margin: '0 auto' }}>
         {localStorage.getItem("loginedUser") === '' ?
        <ol>
            <li><Link to = '/login'>Login</Link></li>
            <li><Link to='/signup'>SignUp</Link></li>
        </ol>
        :
        <ol>
            <li><Link to='/logout' onClick={() => {
                localStorage.setItem("loginedUser","")
                history.push("/user")
                }}>Logout</Link></li>
            <li><Link to='/user-list'>UserList</Link></li>
            <li><Link to='/user-detail'>UserDetail</Link></li>
            <li><Link to='/user-edit'>UserEdit</Link></li>
            <li><Link to='/user-remove'>UserRemove</Link></li>
            
        </ol>
        
    }</nav>
    )};

export const ItemMenu = () => (  
    <nav style = {{ width: '500px', margin: '0 auto' }}>
        <ol>
            <li><Link to = '/item-list'>ItemList</Link></li>
            <li><Link to = '/item-register'>ItemRegister</Link></li>
            <li><Link to = '/item-detail'>ItemDetail</Link></li>
            <li><Link to = '/item-remove'>ItemRemove</Link></li>
        </ol>
    </nav>
);

export const BoardMenu = () => (  
    <nav style = {{ width: '500px', margin: '0 auto' }}>
        <ol>
            <li><Link to = '/post-list'>PostList</Link></li>
            <li><Link to = '/post-write'>PostWrite</Link></li>
            <li><Link to = '/post-modify'>PostModify</Link></li>
            <li><Link to = '/post-remove'>PostRemove</Link></li>
        </ol>
    </nav>
);

export const ArticleMenu = () => (
    <nav style = {{ width: '500px', margin: '0 auto' }}>
        <ol>
            <li><Link to = '/article-lilst'>ArticleList</Link></li>
            <li><Link to = '/article-write'>ArticleWrite</Link></li>
            <li><Link to = '/article-read'>ArticleRead</Link></li>
            <li><Link to = '/article-remove'>ArticleRemove</Link></li>
        </ol>
    </nav>
);

/*
{localStorage.getItem('loginedUser') === '' ?
        <ol>
            <li><Link to = '/login'>Login</Link></li>
            <li><Link to = '/signup'>SignUp</Link></li>
        </ol>
        :
        */