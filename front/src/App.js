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
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom"
class App extends React.Component{
  constructor(props){
      super(props)
      this.state = { // state - состояние
           'users': [],
           'todos': [],
           'projects': []
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

    axios.get('http://127.0.0.1:8000/api/todo/').then(response =>{
      this.setState(
        {
          'todos':response.data
        }
      )

    }).catch(error=> console.log(error))

    axios.get('http://127.0.0.1:8000/api/project/').then(response =>{
      this.setState(
        {
          'projects':response.data
        }
      )

    }).catch(error=> console.log(error))

  }
  render(){
       return(
         <div>
          <div><Menu/></div>
          {/* <Route exact path='/' element={<Navigate to='/authors'/>}/>
            <Route path='/authors'>
              <Route index element={<AuthorsList authors={this.state.authors}/>}/>
              <Route path=':authorId' element={<BookAuthors books={this.state.books}/>}/>
            </Route>
            <Route exact path='/books' element={<BookList books={this.state.books}/>}/> */}
          <BrowserRouter>
          <Routes>
          <Route exact path='/' element={<Navigate to='/users'/>}/>
          <Route path='/users'>
            <Route index element={<div><UsersList users={this.state.users}/></div>}/> 
            <Route path=':userId' element={<ProjectsUser projects={this.state.projects}/>}/>
          </Route>
            {/* <Route exact path='/users' element={<div><UsersList users={this.state.users}/></div>}/> */}
            <Route exact path='/todos' element={<div><TodoList todos={this.state.todos}/></div>}/>
            <Route exact path='/projects' element={<div><ProjectsList projects={this.state.projects}/></div>}/> 
           </Routes>
         </BrowserRouter>  
         <div><Futer/></div>
         </div>     
       )

  }

}
export default App;
