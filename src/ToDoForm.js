import React from 'react'
import shortid from 'shortid'
class ToDoForm extends React.Component{
constructor() {
super();
this.state = {
          text:''
        };
        
      }
   
  

  

    handleChange = (e) => {
        // console.log("handleChange")
        e.preventDefault()
        this.setState({[e.target.name]:e.target.value});
        // console.log("state:", this.state)
        // console.log("value:", e.target.value,"name",e.target.name)

    }

    handleSubmit = (e) => {
        console.log("handleSubmit")
        e.preventDefault();
        this.props.onSubmit({
            id: shortid.generate(),
            text: this.state.text,
            complete: false
        })
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
            <button onClick={this.handleSubmit}>Add Task to do</button>
            
            </form>
        )
    }
}

export default ToDoForm;