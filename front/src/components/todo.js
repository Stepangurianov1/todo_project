import React from "react";
import "./menu.css"
// import "./users.css"
const Todo = ({todo}) => {

    return(
        <tr>
            <td>
                {todo.id}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.data_create}
            </td>
            <td>
                {todo.data_update}
            </td>
            <td>
                {todo.is_active}
            </td>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.user}
            </td>
            
        </tr>
    )

}

const TodoList = ({todos}) => {

    return(
        <table class='table'>
            <tr>
            <th>
                Id
            </th>
            <th>
                Text
            </th>
            <th>
                Data Create
            </th>
            <th>
                Data Update
            </th>
            <th>
                Active
            </th>
            <th>
                Project ID
            </th>
            <th>
                User Id
            </th>
            </tr>
            {todos.map((todo)=> <Todo todo={todo}/>)}
        </table>
    )
}

export default  TodoList;