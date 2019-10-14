import React from 'react'
import ToDoForm from './ToDoForm';
import Todo from './Todo'
import Today from './Today'
import ThisWeek from'./ThisWeek'

class ToDoList extends React.Component{
    constructor() {
        super();
        this.state = {
        todos:[],
        todoToShow:'all',
        priorityToShow:'all'
    }
}

componentDidMount(){
  console.log("hello")
  
}

    addTodo = (todo) => {
        //add todo to current state of todos 
        this.setState({
            todos: [todo,...this.state.todos]
        });
        console.log("TODOS ======>", this.state.todos)
    }

    toggleComplete = id => {
        console.log("toggleComplete")
        this.setState(state => ({
          todos: state.todos.map(todo => {
            if (todo.id === id) {
              
              return {
                ...todo,
                complete: !todo.complete
              };
            } else {
              return todo;
            }
          })
        }));
      };

      updateTodoToShow = (s) =>{
          this.setState({todoToShow:s})
      }

      handleDelete = id =>{
          this.setState({ 
          todos : this.state.todos.filter(todo =>todo.id !== id)
          });
    }

    removeCompleteTodos = id => {
        this.setState({todos : this.state.todos.filter(todo => !todo.complete)


        });
    }
    
      
      render() {

        // let  doToday = this.state.toDo

        let todos = [];
        

        if(this.state.todoToShow === 'all'){
            todos = this.state.todos;
        }else if(this.state.todoToShow === 'active') {
            todos = this.state.todos.filter(todo => !todo.complete)
        }else if(this.state.todoToShow === 'complete') {
            todos = this.state.todos.filter(todo => todo.complete)
        }
        return (
            
          <div className="">
              <h1 className="heading"> Todo List </h1>
              <ToDoForm onSubmit={this.addTodo}/>
              {todos.map(todo => (
                  <Todo key={todo.id} todo={todo} 
                  toggleComplete={()=> this.toggleComplete(todo.id)}
                  onDelete={() => this.handleDelete(todo.id)}
                  text={todo.text}
                  priority={todo.priority}/>
              ))}
              <div style = {{ display: "flex", justifyContent:'left' }}>
              to do today : 
              {this.state.todos.filter(todo => todo.priority === 'today').map(todo => (
                <Today key={todo.id} todo={todo} text={todo.text}/>
              ))}
              </div>
              <div>
              to do this week : 
              {this.state.todos.filter(todo => todo.priority === 'this week').map(todo => (
                <ThisWeek key={todo.id} todo={todo} text={todo.text}/>
              ))}
              </div>
              <div>
                  todos left : 
                  {this.state.todos.filter(todo => !todo.complete).length}
              </div>
              <button onClick={()=> {this.updateTodoToShow('all')}}>All</button>
              <button onClick={()=> {this.updateTodoToShow('active')}}>active</button>
              <button onClick={()=> {this.updateTodoToShow('complete')}}>complete</button>
              {this.state.todos.some(todo => todo.complete) ? <div>
                  <button onClick={this.removeCompleteTodos}> remove completed todos</button>
              </div> : null}
            
            
          </div>
        )
      }
    }
    
export default ToDoList;