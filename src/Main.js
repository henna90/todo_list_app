import React from 'react'
// import Access from './Access';
import axios from 'axios';
import cookie from 'react-cookies'

// import Todolist from './Todolist'
import Login from './Login';
import Register from './Register';

import List from './List'


import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


class Main extends React.Component{
constructor() {
    super();
    this.state = {
        loggedIn:'false',
        access_token:''
        } 
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleClick = this.handleClick.bind(this)
      }


      componentDidMount(){
        console.log("=============>",cookie.load('access_token'))
          console.log(this.props.loggedIn)
        //   this.setState({loggedIn: this.props.loggedIn})
          if(cookie.load('access_token')){
              console.log("logged in !")
             
            this.setState({loggedIn:'true'})
          }
          
      }
   
      handleClick(event){
          console.log("HAND CLICK CLICKED")

          // redirect to registration page 
          event.preventDefault()
      }

      handleSubmit(event){
    
        event.preventDefault();
        alert("submitted")
    
        let data = {'username': event.target.username.value,
                    'password': event.target.password.value}
        
        axios.post("http://127.0.0.1:5000/login",data)   
        .then(data => {
            if(data.data.access_token === undefined){
               alert(data.data.message)
               
            }else{
                this.setState({loggedIn:'true'})
            }

        cookie.save('Access Token', data.data.access_token, { path: '/' })
        console.log("added to cookies" ,cookie.load('Access Token'))
   
        // this.setState({access_token: data.data.access_token})
      
        })
        .catch(function (error) {
                console.log(error);
                alert("Your were not able to login because:" ,error)
                  });
        
        
    
    
    }


    render(){

        if(this.state.loggedIn === 'true'){
            return(
                <List />
            )
        }else {
        return(
            
            <Login />
           
        //     <Router>
        //             <div className="nav">
        //             <Link to="/Login">Login</Link>
        //             </div>
        //             <br />
            
        //             <Link to="/Registration">Register</Link>
              
        //         <Switch>
        //             <Route path="/login">
        //                 <Login />
        //             </Route>    
        //             <Route path="/Registration">
        //                 <Register />
        //             </Route>
        //         </Switch>

        //    </Router>

        )
    }
}
}

export default Main;