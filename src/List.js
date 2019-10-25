import React from 'react'


class List extends React.Component{



  render(){
      return (<div className="todo">
        <button value={this.props.id} name={this.props.todo} onClick={this.props.deleteToDo}></button>
      <h1>{this.props.todo}</h1> <br/>
      {this.props.description}
    </div>)
  }
}

export default List;