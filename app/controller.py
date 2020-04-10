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
        #userna = UserModel.user_add(data)
        #sername = request.args['username']
        #password = request.args['password']
        return UserModel.user_add(data)