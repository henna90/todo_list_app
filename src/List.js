import React from 'react'


class List extends React.Component{



  render(){
      return (<ul>
        {/* <button value={this.props.id} name={this.props.todo} onClick={this.props.deleteToDo}></button> */}
        <li className="task">Task : {this.props.todo} <br/> Description:{this.props.description}<span><button className="done" value={this.props.id} name={this.props.todo} onClick={this.props.deleteToDo}>X</button></span> </li>
      
      </ul>)
  }
}

export default List;