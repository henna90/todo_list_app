import React from 'react'
// import axios from 'axios'
// import cookie from 'react-cookies'
// import Todolist from './Todolist'
class Addtodo extends React.Component{


// handleSubmit(event){

//     var token = cookie.load("Access Token");

//     axios.defaults.headers.common = { Authorization: `Bearer ${token}` };

//     const data = {'task': event.target.task.value,
//                    'description': event.target.description.value }
//                    axios
//                    .post("http://127.0.0.1:5000/addtask",data)
//                    .then(response => {
//                      console.log(response.data, "=================++++++++++");
                     
//                    })
//                    .catch(error => {
//                      console.log(error);
//                    });
//     event.preventDefault()
// }  

// addItem(event){
//     // this.addToDo(event)

//     this.props.addToDo()

//     console.log("Add item")
//     event.preventDefault()

// }

render(){
    return(
        <div className="form">
        <form onSubmit={this.props.addToDo}>
            <label>
                Task
                <input type="text" name="task" />
            </label>
            <label>
                description:
                <input type="text" name="description" />
            </label>
            
            <input type='Submit'/>

            {/* <a href="/registeration"> Click here to Register</a>
            <div>Register</div> */}
            
        </form>  
    
        </div>
    )
}    

}
export default Addtodo;