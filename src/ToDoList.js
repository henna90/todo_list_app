import React from "react";
import axios from "axios";
import cookie from "react-cookies";
// import Addtodo from './Addtodo'
// import { thisExpression } from "@babel/types";

class Todolist extends React.Component {
  constructor() {
    super();
    this.state = {
      todos: []
    };
    this.onDelete = this.onDelete.bind(this);
  }

  componentDidMount() {
    console.log("===============", cookie.load("Access Token"));
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
  }



  onDelete(event) {
    const taskId = parseInt(event.target.value);
    this.setState({
      todos: this.state.todos.filter(todo => todo.taskId !== taskId)
    });
    let data = { task_id: event.target.value };

    axios
      .post("http://127.0.0.1:5000/deletetask", data)
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.log(error);
      });

    // for (var i = 0; i < this.state.todos.length; i++) {
    //   if (this.state.todos[i]["taskId"] == event.target.value) {
    //     this.state.todos.splice(i, 1);
    //   }
    // }
    event.preventDefault();
  }

  render() {
    const todos = this.state.todos.map(todo => (
      <div className="form" key={todo.taskId}>
        Task:
        <p>{todo.task}</p>
        Description:
        <p>{todo.description}</p>
        <button onClick={this.onDelete} value={todo.taskId}>
          {" "}
          X{" "}
        </button>
      </div>
    ));

    return( 
      <div>
        {/* <Addtodo /> */}
        {todos}
      </div>
    )
  }
}

export default Todolist;
