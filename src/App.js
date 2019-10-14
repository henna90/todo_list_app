import React from 'react';
// import logo from './logo.svg';
import './App.css';
// import AddItem from './AddItem'
// import DisplayTask from'./DisplayTask'
import ToDoList from'./ToDoList'

class App extends React.Component {

  render() {
    return (
      <div className="App">
        <ToDoList />
      </div>
    )
  }
}

export default App;
