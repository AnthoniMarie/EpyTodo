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
    def user_add(data, username, password):
        try:
            cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
            cursor.connection.commit()
            return jsonify(result="successfully created account")
        except:
            return jsonify(error="an error occured")
    def verif_user_existence(data, username):
        try:
            cursor.execute("SELECT * FROM user WHERE username = (%s)", (username,))
            existence = cursor.fetchone()
            if existence:
                print ("user exist")
                return jsonify(result="successfully checked account")
        except:
            return jsonify(error="an error occured")
    def verif_user_credentials(data, username, password):
        try:
            cursor.execute("SELECT * FROM user WHERE username = (%s) AND password = (%s)", (username, password,))
            is_ok = cursor.fetchone()
            if is_ok:
                print ("user authenticated")
                return jsonify(result="successfully checked user credentials")
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
    def display_task(data):
        cursor.execute("SELECT * FROM task;")
        data = cursor.fetchall()
        return jsonify(task=data)