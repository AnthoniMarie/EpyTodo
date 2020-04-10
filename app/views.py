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
                           myContent="What a beautiful To do list")
@app.route('/brice', methods=['GET'])
def route_brice():
    return render_template("index.html", title="BRICE TITLE",
                           myContent="BRICE CONTENT")
@app.route('/api/users/all', methods=['GET'])
def get_users_list():
    return models.UserModel.get_users_list(db_linkage)
@app.route('/api/users/add', methods=['GET', 'POST'])
def add_user():
    return models.UserModel.user_add(db_linkage)
@app.route('/register', methods=['GET', 'POST'])
def add_user_noapi():
    return controller.UserController.user_add(db_linkage)
    #return render_template("auth/register.html", title="EPyTodo | Connexion :)",
     #                      myContent="Connexion à l'espace membre EPyTodo")
#@app.route('/user')
#def route_all_users():
#    result = ""
#    try:



