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
    return "Helloooo world!\n"
@app.route('/brice', methods=['GET'])
def route_brice():
    return render_template("index.html", title="BRICE TITLE",
                           myContent="BRICE CONTENT")
@app.route('/api/users/all', methods=['GET'])
def get_users_list():
    return models.User_gesture.get_users_list(db_linkage)
#@app.route('/user')
#def route_all_users():
#    result = ""
#    try:



