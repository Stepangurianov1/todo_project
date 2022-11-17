import React from "react";
import "./menu.css"
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom"
const Menu =() =>
{
    return (
        <BrowserRouter>
        <nav>
        <ul class="menu">
            <li>
                <a href="/todos">Todo</a>
            </li>
            <li>
                <a href="/projects">Project</a>
            </li>
            <li>
                <a href="/users">Users</a>
            </li>
        </ul>
        </nav>
        </BrowserRouter>
    )
}


export default  Menu;