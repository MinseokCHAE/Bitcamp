import React from 'react'
import {BrowserRouter as Router, Link} from "react-router"

const App = () => {
  return <>
  <nav>
      <Link to="./index.html">Home</Link>
      <Link to="./blog_list.html">Blog</Link>
      <Link to="./about_me.html">About Me</Link>
    </nav>
    <h1>1st headline</h1>
    <h2>2nd headline</h2>
    <h3>3rd headline</h3>
    <h4>4th headline</h4>
    <h5>5th headline</h5>
    <p>Use p for paragraph</p>
    <Link to="https://www.google.com">Go to google</Link>
    <hr/>
    <img src="./images/stay_funky.jpg" width="600px"></img>
  </>
}

export default App
