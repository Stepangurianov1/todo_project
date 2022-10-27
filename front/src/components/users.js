import React from "react";
import "./menu.css"
import "./users.css"
const User = ({user}) => {

    return(
        <tr>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.birthday_year}
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