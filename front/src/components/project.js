import React from "react";
import "./menu.css"
import "./users.css"
const Project = ({project}) => {

    return(
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                {project.name}
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )

}

const ProjectsList = ({projects}) => {

    return(
        <table class='table'>
            <tr>
            <th>
                ID
            </th>
            <th>
                name
            </th>
            <th>
                Users
            </th>
            </tr>
            {projects.map((project) => <Project project={project}/>)}
        </table>
    )
}

export default  ProjectsList;