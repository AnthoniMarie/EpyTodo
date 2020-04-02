#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## epytodo
## File description:
## __init__.py
##

import os
from flask import *
from app import views

app = Flask(__name__)
app.config.from_object('config')

def test():
    return app