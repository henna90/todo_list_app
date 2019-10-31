import React from "react";
import Addtodo from "./Addtodo";
import List from "./List";
import axios from "axios";
import cookie from "react-cookies";
import Logout from './Logout'
import 'bootstrap/dist/css/bootstrap.css';


class Container extends React.Component {
  constructor() {
    super();
    this.state = {
      todo: [],
      loggedOut: false
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleDelete = this.handleDelete.bind(this);
    this.handleLogout = this.handleLogout.bind(this)
  }

  getToken() {
    console.log("=========ACCESS TOKEN",cookie.load("Access Token") )
    return cookie.load("Access Token");
    
  }

  componentDidMount() {
    const token = this.getToken();
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
  }

  handleSubmit(event) {
    let token = this.getToken();
    console.log(token);

    axios.defaults.headers.common = { Authorization: `Bearer ${token}` };

    const data = {
      task: event.target.task.value,
      description: event.target.description.value
    };
    axios
      .post("http://127.0.0.1:5000/addtask", data)
      .then(response => {
        this.componentDidMount();
        console.log(this.state.todos, "+++++++++++++");
      })
      .catch(error => {
        console.log(error);
      });
    event.preventDefault();
  }

  handleDelete(event) {
    this.setState({
      todos: this.state.todos.filter(todo => todo.task !== event.target.name)
    });
    let token = cookie.load("Access Token");

    axios.defaults.headers.common = { Authorization: `Bearer ${token}` };
    const data = { task_id: event.target.value, task: event.target.name };

    axios
      .post("http://127.0.0.1:5000/deletetask", data)
      .then(response => {
        this.setState({
          todos: this.state.todos.filter(
            todo => todo.taskId !== Number(data["task_id"])
          )
        });
        this.setState({
          todos: this.state.todos.filter(todo => todo.task !== data["task"])
        });
      })
      .catch(error => {
        console.log(error);
      });
    event.preventDefault();

    console.log(event.target.name);
  }

  handleLogout(event){
    alert("logout was clicked")
    cookie.remove("Access Token",{ path: '/' })
    this.setState({loggedOut: true})
    event.preventDefault()
  }

  render() {
    let todos = [];
    if (this.state.todos !== undefined) {
      console.log(todos, "???????????????");
      todos = this.state.todos;
    }
    if(this.state.loggedOut === true){
      return <Logout />
    }

    return (
      <div>
        
        <button className="logout" onClick = {this.handleLogout}>Log out</button>
       
        <Addtodo addToDo={this.handleSubmit} />
        {/* <Todolist todo={todo.task}/> */}
        {todos.map(todo => (
          <List
            key={todo.taskId}
            todo={todo.task}
            description={todo.description}
            id={todo.taskId}
            deleteToDo={this.handleDelete}
          />
        ))}
      </div>
    );
  }
}

export default Container;
