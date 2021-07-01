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

  return (<>
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>User ID</TableCell>
            <TableCell align="right">Password</TableCell>
            <TableCell align="right">User Name</TableCell>
            <TableCell align="right">User Email</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          { user.length != 0
           ? user.map((user) => (
               <TableRow key={user.userid}>
               <TableCell component="th" scope="row">
               {user.userid}
               </TableCell>
               <TableCell align="right">{user.password}</TableCell>
               <TableCell align="right">{user.name}</TableCell>
               <TableCell align="right">{user.email}</TableCell>
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
        <Pagination count={10} />
        <Pagination count={10} color="primary" />
        <Pagination count={10} color="secondary" />
        <Pagination count={10} disabled />
    </div>
    </>);
}

export default UserList
