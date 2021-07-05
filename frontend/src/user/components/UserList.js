import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Pagination from '@material-ui/lab/Pagination';
import { userList } from 'api'


const useStyles = makeStyles({
  table: {
    minWidth: 650,
  },
  
});
const usePageStyles = makeStyles((theme) => ({
    root: {
      '& > *': {
        marginTop: theme.spacing(2),
      },
    },
  }));



const UserList = () => {
  
  const [user, setUser] = useState([])

  const classes = useStyles();
  const pageClasses = usePageStyles();

  useEffect(() => {
    userList()
    .then(res => {
        console.log(res.data)
        setUser(res.data)
    })
    .catch(err => {
        console.log(err.data)
    })
  }, [])

  const handleClick = user => {
    localStorage.setItem("selectedUser", user)
  }


  return (<>
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell align='center'>User ID</TableCell>
            <TableCell align="center">Password</TableCell>
            <TableCell align="center">User Name</TableCell>
            <TableCell align="center">User Email</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          { user.length != 0
           ? user.map((user) => (
               <TableRow key={user.userid}>
               <TableCell align='center' component="th" scope="row">{user.userid}</TableCell>
               <TableCell align="center">{user.password}</TableCell>
               <TableCell align="center">{user.name}</TableCell>
               <TableCell align="center">{user.email}</TableCell>
           </TableRow>
           ))
          :  <TableRow>
          <TableCell component="th" scope="row" colSpan="4">
             <h1>No Data</h1>
          </TableCell>
        
      </TableRow>
          }
        </TableBody>
      </Table>
    </TableContainer>
    <div className={pageClasses.root}>
        <Pagination count={10} color="primary" />
    </div>
    </>);
}

export default UserList
