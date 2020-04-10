#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## epytodo
## File description:
## models.py
##

from flask import *
from config import *
from app import *
import pymysql as sql
import hashlib

class UserModel(object):
    def get_users_list(data):
        request = cursor.execute("SELECT * FROM user;")
        data = cursor.fetchall()
        return jsonify(username=data)
    def user_add(data):
        try:
            username = request.form['username']
            print ("LE USER =", username)
            cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, "pass_test"))
            cursor.connection.commit()
            return jsonify(result="successfully created account")
        except:
            return jsonify(error="an error occured")

class TaskModel(object):
    def task_add(data):
        try:
            title = request.args['title']
            #end  = cursor.execute("SELECT TIMESTAMP('2020-12-01');")
            #begin = cursor.execute("SELECT TIMESTAMP('2001-09-11');")
            #begin = request.args['begin']
            #end = request.args['end']
            #status = request.args['status']
            cursor.execute("INSERT INTO task (title) VALUES (%s)", (title))
            cursor.connection.commit()
            return jsonify(result="Task created successfully")
        except:
            return jsonify(result ="an error occured")
