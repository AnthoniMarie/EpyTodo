#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## epytodo
## File description:
## controller.py
##

from app import *
from flask import *
from app.models import UserModel
from config import *
import pymysql as sql
import hashlib

class UserController(object):
    def user_add(data):
        username = request.form.get('username', data)
        password = request.form.get('password', data)
        #username = request.args['username']
        #print ("Le user est :" + username)
        #print (request.form.getlist(key=db_linkage))
        #username = request.form.get['username']
        #userna = UserModel.user_add(data)
        #username = request.args['username']
        #password = request.args['password']
        return render_template("auth/register.html", title="EPyTodo | Connexion :)",
                      myContent="Connexion à l'espace membre EPyTodo", data=UserModel.user_add(data, username, password))
