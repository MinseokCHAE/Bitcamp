import React,{useState} from 'react'
import './PostWrite.css'
import { Button } from '@material-ui/core';
import { useHistory } from 'react-router';
import { boardPostWrite } from 'api';


const PostWrite = () => {
  const history = useHistory()
  const [boardInfo, setBoardInfo] = useState({
    title: '',
    content: '',
  })
    
  const { title, content } = boardInfo

  const handleChange = e => {
    const { name, value } = e.target
    setBoardInfo({
      ...boardInfo, [name]: value
        })
    }
    
  const handleSubmit = e => {
    e.preventDefault()
    alert(`accept: ${JSON.stringify({...boardInfo})}`)
    boardPostWrite({...boardInfo})
    .then(res => { alert(`posting success: ${res.data.result}`) 
    //history.push('login')
})
    .catch(err => { alert(`posting failed: ${err}`)})
  }
    
  const handleClick = e => {
    e.preventDefault()
    alert('cancel')
    }
  
  return (<>
  <div className='Signup'>
    <form onSubmit={handleSubmit} method='post' style={{border:"1px solid #ccc"}}>
  <div className="container">
    <h1>Post Write</h1>
    <p>Please fill in this form.</p>
    <hr/>

    <label for="title"><b>Title</b></label>
    <input type="text" placeholder="Enter title" onChange={handleChange} name="title" value={title}/>

    <label for="content"><b>Content</b></label>
    <input type="text" placeholder="Enter content" onChange={handleChange} name="content" value={content}/>


    <div class="clearfix">
      <button type="submit" className="signupbtn">Post</button>
      <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
    </div>
  </div>
  
</form>
</div>
</>)
}

export default PostWrite
