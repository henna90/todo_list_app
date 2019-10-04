import React from 'react'
import shortid from 'shortid'
import $ from 'jquery'; 

class ToDoForm extends React.Component{
constructor() {
super();
this.state = {
          text:''
        //   priority:'today'
        };
        
      }
   
  

  

    handleChange = (e) => {
        
        e.preventDefault()
        this.setState({[e.target.name]:e.target.value});
        
        console.log("======",{[e.target.name]:e.target.value})
        

    }

    handleSubmit = (e) => {
        e.preventDefault();
        this.props.onSubmit({
            id: shortid.generate(),
            text: this.state.text,
            complete: false,
            priority: this.state.priority

        })
        
        const data = {id: shortid.generate(),
            text: this.state.text,
            complete: false,
            priority: this.state.priority}
        console.log("DATA",data)
        $.post("http://localhost:3000/addtask",data)
    .then(response => console.log(response.result))      
        this.setState({text:''});
    }

    render(){
        return(
            <form onSubmit={this.handleSubmit}>
            <input 
            name="text"
            value={this.state.text} 
            onChange={this.handleChange} 
            placeholder="to do..."/>

            <select name="priority" onChange={this.handleChange}>
                <option when="today">today</option>
                <option when="this week">this week </option>
                <option when="whenever">Whenever</option>
            </select>
            
            <button onClick={this.handleSubmit}>Add Task to do</button>
            
            </form>
        )
    }
}

export default ToDoForm;