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
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User_gesture(object):
    def user_add(self):
        request = cursor.execute("SELECT * FROM user");

class Content(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Interger, nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

    db.create_all()
