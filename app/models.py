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

class User_gesture(object):
    def get_users_list(data):
        request = cursor.execute("SELECT * FROM user;")
        data = cursor.fetchall()
        return {"username":data}
    def user_add(data):
        request = cursor.execute("SELECT * FROM user where username = %s");
