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
from datetime import datetime

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
    def task_add(data, title, begin, end, status):
        try:
            cursor.execute("INSERT INTO task (title, begin, end, status) VALUES (%s, %s, %s, %s)", (title, begin, end, status))
            cursor.connection.commit()
            return jsonify(result="Task created successfully")
        except:
            return jsonify(result ="an error occured")
    def display_task(data):
        cursor.execute("SELECT * from task;")
        db_linkage.commit()
        data = cursor.fetchall()
        return data
    def verif_task_existence(data, title):
        try:
            cursor.execute("SELECT * FROM task WHERE title = (%s)", title)
            existence = cursor.fetchone()
            if existence:
                return jsonify(result="Task already exist")
        except:
            return jsonify(error="All is good")
    def task_del(data, task_id):
        try:
            cursor.execute("DELETE FROM task WHERE task_id = (%s)", task_id)
            db_linkage.commit()
            return jsonify(result="Deleted task successfully")
        except:
            print(task_id)
            return jsonify(result="an error occured")