#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## epytodo
## File description:
## views.py
##

from app import *

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def route_home():
    return "Helloooo world!\n"
@app.route('/brice', methods=['GET'])
def route_brice():
    return render_template("index.html", title="BRICE TITLE",
                           myContent="BRICE CONTENT")
