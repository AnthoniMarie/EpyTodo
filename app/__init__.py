#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## epytodo
## File description:
## __init__.py
##

from flask import *
from config import *
import pymysql as sql

app = Flask(__name__)
app.config.from_object('config')

db_linkage = sql.connect(host=DATABASE_HOST,
                      db=DATABASE_NAME,
                      user=DATABASE_USER,
                      password=DATABASE_PASS,
                      unix_socket=DATABASE_SOCK)
cursor = db_linkage.cursor()

def test():
    return app