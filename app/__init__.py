#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## epytodo
## File description:
## __init__.py
##

import os
from flask import *

app = Flask(__name__)
app.config.from_object('config')

def test():
    return app