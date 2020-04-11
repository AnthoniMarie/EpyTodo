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
        username = request.form.get('username', None)
        password_ns = request.form.get('password', None)
        test = UserModel.verif_user_existence(data, username)
        print(test)
        if request.method == "POST" and username and password_ns:
            password = hashlib.sha3_256(str(password_ns).encode('utf-8')).hexdigest()
            UserModel.user_add(data, username, password)
            flash("Création de votre compte réussie :)", "success")
        elif request.method == "POST":
            flash("Echec de la création de votre compte :(, vérifiez les informations saisies", "error")

        return render_template("auth/register.html", title="EPyTodo | Inscription :)",
                      myContent="S'inscrire à l'espace membre EPyTodo")
    def user_login(data):
        print ("test")
        return render_template("auth/login.html", title="EPyTodo | Connexion :)",
                               myContent="Connexion à l'espace membre EPyTodo")
