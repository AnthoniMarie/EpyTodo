#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## epytodo
## File description:
## views.py
##

from app import *
from app import controller
from app import models
from flask import jsonify
import pymysql as sql

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def route_home():
    return render_template("index.html", title="EPyTodo :)",
                           myContent="main page")
@app.route('/register', methods=['GET', 'POST'])
def add_user_noapi():
    return controller.UserController.user_add(db_linkage)
@app.route('/signin', methods=['GET', 'POST'])
def login_user():
    return controller.UserController.user_login(db_linkage)
@app.route('/signout', methods=['GET', 'POST'])
def logout_user():
    return controller.UserController.user_logout(db_linkage)
@app.route('/user/task', methods=['GET', 'POST'])
def task_list():
    return controller.TaskController.task_list(db_linkage)
@app.route('/user/task/add', methods=['GET', 'POST'])
def task_add():
    return controller.TaskController.task_add(db_linkage)
@app.route('/user/task/del/<task_id>', methods=['GET', 'POST'])
def task_del(task_id):
    return controller.TaskController.task_del(db_linkage, task_id)