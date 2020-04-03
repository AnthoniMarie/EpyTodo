#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## epytodo
## File description:
## __init__.py
##

import os
from flask import *
from config import *
import pymysql as sql

app = Flask(__name__)
app.config.from_object('config')

connect = sql.connect(host=DATABASE_HOST,
                      db=DATABASE_NAME,
                      user=DATABASE_USER,
                      password=DATABASE_PASS,
                      unix_socket=DATABASE_SOCK)
cursor = connect.cursor()

def test():
    return app