# EPyTodo - Make your own MVC website in Python with Flask !

![build with Python](https://img.shields.io/badge/Build%20with-Python-green)
![version](https://img.shields.io/badge/Version-1.0-brightgreen)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://anthoni-marie.fr">
    <img src="https://s.anthoni-marie.fr/m_w/2021/img/logo-black.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">EPyTodo Project</h3>

  <p align="center">
    EPyTodo is a project which you could rely on in the future.<br />
    The goal was to develop a simple todolist website!
  </p>
</p>


- **Language:** Python 3

# Subject

Into this project, you’ll have to develop:
- your MySQL database scheme
- your web server using Flask
- your HTML pages using Jinja2 (integrated with Flask)

## MySQL Database

Into your database, you’ll need to handle many users with their tasks.

> :exclamation: All instructions have to be **strictly** followed

Create a file named **epytodo.sql**.<br />
You will write into it all your database scheme.<br />
The database name is **epytodo**.<br />
Its tables are named :
- user
- task
- user_has_task

> :bulb: Think about the last one : why do you need this ?<br />
> Maybe it has to do with relationship...

Here are all fields (with types or values) which you must have into your tables:
- user table
  - **_user_id_** (mandatory not null)
  - **_username_** (mandatory not null)
  - **_password_** (mandatory not null)
  - etc.
- task table
  - **_task_id_** (mandatory not null)
  - **_title_** (mandatory not null)
  - **_begin_** (optional value when creating a task, actual date by default)
  - **_end_** (optional value when creating a task, empty by default)
  - **_status_** (**not started** by default / **in progress** / **done**)
  - etc.
- user_has_task table
  - **_fk_user_id_**
  - **_fk_task_id_**

Once your scheme is created, import your file into your MySQL server

```
∼/B-WEB-200> cat epytodo.sql | mysql -u root -p
```

> :exclamation: Your sql file has to be placed at the root folder when turned in.<br />
> Do not insert any records into this file

## Web Server

Files to turn in (refer to the bootstrap to know where placing them into your folders):
- **run.py**
- **&#95;&#95;init&#95;&#95;.py**
- **models.py**
- **views.py**
- **controller.py**

You server will implement a MVC architecture.<br />
There’s not only ONE way to implement it but it’s **mandatory** to do so.<br />
Look closely at schemes you can find. Here’s a [TIP].<br />

More explanations of what is attempted into each file:
- **_run.py_** : your entry program
- **_&#95;&#95;init&#95;&#95;.py_** : your app package file
- **_models.py_** : all objects / functions which will interact with your database
- **_views.py_** : all routes which are described into the API file
- **_controller.py_** : all interactions between your views and your models

We will add our **_config.py_** file.

All settings for your program (debug mode, database configuration, etc.) will be there!
Here are the required ones :
- **_DATABASE_NAME_**
- **_DATABASE_HOST_**
- **_DATABASE_SOCK_**
- **_DATABASE_USER_**
- **_DATABASE_PASS_**

Be sure that your **_config.py_** is similar and used effectively.

## HTML pages

All data will transit into JSON format (see API file).<br />
You are free to display all information as you want (plain text, lists, accordion, etc.).<br />
This graphical part will be evaluated during your presentation.

# Bonus

> :exclamation: Do not integrate any extra features like allowing PUT or DELETE methods into your main delivery.<br />
> Do this into a bonus directory

Here is a minimal list of what you can do as a bonus:
- add a responsive design
- develop more functionalities than expected:
  - Ajax requests
  - dynamic components (drag & drop cards, datepickers, etc.)
  - contacts system (adding friends, authorizations handling, etc.)
  - notifications
- implement a real login system (OAuth / SSO / LDAP / etc.)
- develop what’s in your mind

# Table of content
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [EPyTodo - A web ToDo app](#epytodo-a-web-todo-app)
- [Subject](#subject)
	- [MySQL Database](#mysql-database)
	- [Web Server](#web-server)
	- [HTML pages](#html-pages)
- [Bonus](#bonus)
- [Table of content](#table-of-content)

<!-- /TOC -->

[TIP]: http://lmgtfy.com/?q=MVC
