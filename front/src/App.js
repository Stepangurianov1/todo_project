import logo from './logo.svg';
import './App.css';
import React from "react"
import UsersList from './components/users';
import axios from "axios"
import Menu from './components/menu';
import Futer from './components/footer';
import TodoList from './components/todo';
import ProjectsList from './components/project';
import ProjectsUser from './components/project_user';
import LoginForm from './components/auth';
import Cookies from 'universal-cookie';
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom"
class App extends React.Component{
  constructor(props){
      super(props)
      this.state = { // state - состояние
           'users': [],
           'todos': [],
           'projects': [],
           'token': '',
      }
  }

  logout(){

    this.set_token('')
    // this.setState({'books':[], 'authors':[]})
  }

  is_auth(){
    // console.log(this.state.token)
    return !!this.state.token

  }

  set_token(token){
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token':token}, ()=>this.load_data())
  }

  get_token_storage(){ 
    const cookie = new Cookies()
    const token = cookie.get('token')
    this.setState({'token':token}, () => this.load_data())

  }

  get_token(username, password){

    const data = {username:username, password:password}
    axios.post('http://127.0.0.1:8000/api-token-auth/', data).then(response => {
      this.set_token(response.data['token'])
    }).catch(error => alert('Неверный логин или пароль'))
  }

  get_headers(){
    let headers = {
      'Content-Type': 'application/json'
      }
      // console.log(this.is_auth())
      if (this.is_auth())
      {
      headers['Authorization'] = 'Token ' + this.state.token
      }
      return headers
      
  }
  load_data(){
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response =>{
      this.setState(
        {
          'users':response.data
        }
      )

    }).catch(error=> console.log(error))

    axios.get('http://127.0.0.1:8000/api/todo/', {headers}).then(response =>{
      this.setState(
        {
          'todos':response.data
        }
      )

    }).catch(error=> console.log(error))

    axios.get('http://127.0.0.1:8000/api/project/', {headers}).then(response =>{
      this.setState(
        {
          'projects':response.data
        }
      )

    }).catch(error=> console.log(error))

  }
  componentDidMount(){ //устанавливает состояние. когда подтягивается компонент заходим сюда отрабатывает когда запрашиваем данные
    this.get_token_storage()
  }
  render(){
      console.log(this.is_auth())
       return(
         <div>
          <div><Menu/>{this.is_auth() ? <button onClick={()=> this.logout()}>Logout</button> : <a href='/login'>Login</a>}</div>

          <BrowserRouter>
          <Routes>
          <Route exact path='/' element={<Navigate to='/users'/>}/>
          <Route path='/users'>
            <Route index element={<div><UsersList users={this.state.users}/></div>}/> 
            <Route path=':userId' element={<ProjectsUser projects={this.state.projects}/>}/>
          </Route>
            <Route exact path='/todos' element={<div><TodoList todos={this.state.todos}/></div>}/>
            <Route exact path='/projects' element={<div><ProjectsList projects={this.state.projects}/></div>}/> 
            <Route exact path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)}/>}/>
           </Routes>
         </BrowserRouter>  
         {/* <div><Futer/></div> */}
         </div>     
       )

  }

}
export default App;
