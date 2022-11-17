import React from "react";
import "./menu.css"
import "./users.css"
import { Link } from 'react-router-dom'
const User = ({user}) => {

    return(
        <tr>
            <td>
            <Link to={`/users/${user.id}`}>{user.first_name}</Link>
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.email}
            </td>
            <td>
                {user.username}
            </td>
        </tr>
    )

}

const UsersList = ({users}) => {

    return(
        <table class='table'>
            <tr>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                birthday_year
            </th>
            <th>
                Email
            </th>
            <th>
                Name
            </th>
            </tr>
            {users.map((user) => <User user={user}/>)}
        </table>
    )
}

export default  UsersList;