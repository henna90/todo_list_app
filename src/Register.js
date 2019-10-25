import React from 'react'
// import $ from 'jquery';
// import axios from 'axios';


export default class Register extends React.Component {
  constructor() {
    super();
    this.state = {
       
        } 
        this.handleRegister = this.handleRegister.bind(this);
      }

      handleRegister(event){
        event.preventDefault()
        console.log("REGISTRATION")
        // send post request to register

      }

  // componentDidMount() {
   

  //   axios.get("http://127.0.0.1:5000/test", {headers: Authoization : })
  //     .then(response => {
  //      console.log(response)
  //     })
  // }

  render() {
    return (
      <div className="form">
      <form onSubmit={this.handleRegister}>
      <label>
          Username:
          <input type="text" name="username" value={this.state.value} onChange={this.handleUsername}/>
      </label>
      <br />
      <label>
          Password:
          <input type="text" name="password" value={this.state.value} onChange={this.handlePassword}/>
      </label>
      <br />
      <label>
          confirm password:
          <input type="text" name="repeat-password" value={this.state.value} onChange={this.handleRepeatPassword}/>
      </label>
      <input type='submit'/>
      
  </form> 
  </div>
    )
  }
}

// export default Register;