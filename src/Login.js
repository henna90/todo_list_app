import React from 'react'
// import $ from 'jquery';
import axios from 'axios';

import Container from './Container'
// import Addtodo from './Addtodo'
// import { Redirect } from 'react-router-dom'

// import ToDoForm from './ToDoForm';
// import Todo from './Todo'
// import Today from './Today'
// import ThisWeek from'./ThisWeek'
// import { useCookies } from 'react-cookie';

import cookie from 'react-cookies'
// import { inferredPredicate } from '@babel/types';

class Login extends React.Component{
    constructor() {
        super();
        this.state = {
            loggedIn:'false'
    
    }
    this.handleSubmit = this.handleSubmit.bind(this);  
}




// componentDidMount() {
//     console.log("===============", cookie.load("Access Token"));
//     var token = cookie.load("Access Token");

//     axios.defaults.headers.common = { Authorization: `Bearer ${token}` };

//     axios
//       .get("http://127.0.0.1:5000/todos")
//       .then(response => {
//         console.log(response.data, "=================++++++++++");
//         this.setState({ todos: response.data });
//       })
//       .catch(error => {
//         console.log(error);
//       });
//   }


handleSubmit(event){
    
    event.preventDefault();
    alert("submitted")

    let data = {'username': event.target.username.value,
                'password': event.target.password.value}
    
    axios.post("http://127.0.0.1:5000/login",data)   
    .then(data => {
        if(data.data.access_token === undefined){
           alert(data.data.message)
        }
    cookie.save('Access Token', data.data.access_token, { path: '/' })
    console.log("added to cookies" ,cookie.load('Access Token'))
    this.setState({loggedIn:'true'})
     var token = cookie.load("Access Token");

    axios.defaults.headers.common = { Authorization: `Bearer ${token}` };

    axios
      .get("http://127.0.0.1:5000/todos")
      .then(response => {
        console.log(response.data, "=================++++++++++");
        this.setState({ todos: response.data });
      })
      .catch(error => {
        console.log(error);
      });
  
    })
    .catch(function (error) {
            console.log(error);
            alert("Your were not able to login because:" ,error)
            
              });
    
    


}
    
   
    

render() {
    if(this.state.loggedIn === 'true'){
        return (
            <div>
            {/* <Addtodo /> */}
            <Container />
            </div>
        )
    }else{
    
    return (
        <div className="form">
        <form onSubmit={this.handleSubmit}>
            <label>
                Username:
                <input type="text" name="username" value={this.state.value} onChange={this.handleUsername}/>
            </label>
            <label>
                Password:
                <input type="text" name="password" value={this.state.value} onChange={this.handlePassword}/>
            </label>
            
            <input type='Submit'/>
            
        </form>   
        </div>
    )
}
}
}



    
export default Login;