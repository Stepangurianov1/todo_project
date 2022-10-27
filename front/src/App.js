import logo from './logo.svg';
import './App.css';
import React from "react"
import UsersList from './components/users';
import axios from "axios"
import Menu from './components/menu';
import Futer from './components/footer';
class App extends React.Component{
  constructor(props){
      super(props)
      this.state = { // state - состояние
           'users': []
      }
  }


  componentDidMount(){ //устанавливает состояние. когда подтягивается компонент заходим сюда отрабатывает когда запрашиваем данные
    axios.get('http://127.0.0.1:8000/api/users/').then(response =>{
      this.setState(
        {
          'users':response.data
        }
      )

    }).catch(error=> console.log(error))

  }
  render(){
       return(
         <div>
           <div><Menu/></div>
           <div><UsersList users={this.state.users}/></div>
           <div><Futer/></div>
         </div>
         
       )

  }

}
export default App;
