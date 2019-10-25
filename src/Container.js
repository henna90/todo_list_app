import React from 'react';
import Addtodo from './Addtodo';
// import Todolist from './Todolist';
import List from './List'
import axios from 'axios'
import cookie from 'react-cookies'

class Container extends React.Component {
    constructor() {
        super();
        this.state = {
          todo:[]
            
    
    }
    this.handleSubmit = this.handleSubmit.bind(this);  
    this.handleDelete = this.handleDelete.bind(this);
}

componentDidMount() {
  const token = cookie.load("Access Token");
  console.log(token)
  //set headers for http request
  axios.defaults.headers.common = { Authorization: `Bearer ${token}` };
  axios
    .get("http://127.0.0.1:5000/todos")
    .then(response => {
      this.setState({ todos: response.data });
    })
    .catch(error => {
      console.log(error);
    });
    // console.log(this.state.todos)
}


    handleSubmit(event){
      

            let token = cookie.load("Access Token");
        
            axios.defaults.headers.common = { Authorization: `Bearer ${token}` };
        
            const data = {'task': event.target.task.value,
                           'description': event.target.description.value }
                           axios
                           .post("http://127.0.0.1:5000/addtask",data)
                           .then(response => {
                             console.log(response.data, "=================++++++++++");
                            this.setState({todos:[data,...this.state.todos]})
                            console.log(this.state.todos, "+++++++++++++")
                             
                           })
                           .catch(error => {
                             console.log(error);
                           });
            event.preventDefault()
        }


   handleDelete(event){

  
  //    console.log(">>>>>>>>>", event.target.value)
  //    console.log(event.target.task.value, "<<<<<<<=======")
  // console.log(event)

    this.setState({todos: this.state.todos.filter(todo => todo.task !== event.target.name)})
    let token = cookie.load("Access Token");
        
    axios.defaults.headers.common = { Authorization: `Bearer ${token}` };
    const data = {'task_id': event.target.value,
                  'task':event.target.name}

    axios.post("http://127.0.0.1:5000/deletetask",data)
                           .then(response => {
                             console.log(response.data, "=================++++++++++");
                             console.log( data['task_id'])
                             this.setState({todos : this.state.todos.filter(todo =>todo.taskId!== Number(data['task_id']))})
                             this.setState({todos: this.state.todos.filter(todo => todo.task !== data['task'])})
                             
                            //  if(event.target.value.length){
                            //    this.setState({todos: this.state.todos.filter(todo => todo.task !== event.target.name)})
                            //  }else {
                            // this.setState({todos : this.state.todos.filter(todo =>todo.taskId!== Number(data['task_id']))})
                            // console.log(this.state.todos, "+++++++++++++")
                            //  }
                           })
                           .catch(error => {
                             console.log(error);
                           });
                           event.preventDefault()

     console.log(event.target.name)
   }     





  render() {
    let todos = []
    if(this.state.todos !== undefined){
      console.log(todos, "???????????????")
      todos = this.state.todos
    }  

      
    return (
      <div>
        <Addtodo addToDo={this.handleSubmit}/>
        {/* <Todolist todo={todo.task}/> */}
        {todos.map(todo => (
          <List key={todo.taskId} todo={todo.task} description={todo.description} id={todo.taskId} deleteToDo={this.handleDelete}/>
          ))}
     
        
      </div>
    );
  }
}

export default Container;
