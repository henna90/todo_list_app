// import React from 'react'
// import Login from './Login';
// import Register from './Register';



// import {
//   BrowserRouter as Router,
//   Switch,
//   Route,
//   Link
// } from "react-router-dom";

// class Access extends React.Component{
    
//     render(){
//         return( 

            
//             <Router>
//           <div className="App">
//             <nav>
//               <ul>
             
//                 <li>
//                   <Link to="/Login" >Login</Link>
//                 </li>
//                 <li>
//                   <Link to="/Register">Register</Link>
//                 </li>
//               </ul>
//             </nav>
    
//             {/* A <Switch> looks through its children <Route>s and
//                 renders the first one that matches the current URL. */}
            
//             <Switch>
//               <Route path="/Login" handLogin={this.props.handleLogin} >
//                 <Login />
//               </Route>
//               <Route path="/Register">
//                 <Register />
//               </Route>

//             </Switch>
//             </div>
//         </Router>
//         )
//     }
// }

// export default Access;