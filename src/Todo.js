import React from 'react'

export default props => (
    <div style = {{ display: "flex", justifyContent:'center' }}>
   
   {/* <div>{props.priority} </div><br /> */}
    <div style={{textDecoration: props.todo.complete ? "line-through": ""}} onClick={props.toggleComplete}>
    {props.text}</div>

    
    <button onClick={props.onDelete}>X</button>
    <div style={{textAlign: "right"}}></div>
    </div>

);
