import React from "react";
import "./menu.css"
import "./users.css"
import { useParams } from 'react-router-dom'
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom"
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

const ProjectsUser = ({projects}) => {
    let {userId} = useParams()
    let filter_project = projects.filter((project)=>project.users.includes(parseInt(userId)))
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
            {filter_project.map((project) => <Project project={project}/>)}
        </table>
    )
}

export default  ProjectsUser;

// const BookAuthors = ({books}) => {
//     let {authorId} = useParams()
//     console.log(authorId)
//     let filter_books = books.filter((book)=>book.authors.includes(parseInt(authorId)))
//     return (
//     <table>
//     <th>
//         Name
//     </th>
//     <th>
//         Authors
//     </th>
//     <th>
//         ID
//     </th>
//     {filter_books.map((book_) => <BookItem book={book_} />)}
//     </table>
//     )
// }
//     export default BookAuthors