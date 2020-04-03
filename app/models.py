#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## epytodo
## File description:
## models.py
##

from flask import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Interger, nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

    db.create_all()
