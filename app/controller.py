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
        if request.method == "POST" and username and password_ns:
            if UserModel.verif_user_existence(data, username) == None:
                password = hashlib.sha3_256(str(password_ns).encode('utf-8')).hexdigest()
                UserModel.user_add(data, username, password)
                flash("Création de votre compte réussie :)", "success")
            else:
                flash ("Un compte avec ce pseudonyme est déjà occupé :/, copieur", "error")
        elif request.method == "POST":
            flash("Echec de la création de votre compte :(, vérifiez les informations saisies", "error")

        return render_template("auth/register.html", title="EPyTodo | Inscription :)",
                      myContent="register a new user")
    def user_login(data):
        password = hashlib.sha3_256(str(request.form.get('password', data)).encode('utf-8')).hexdigest()
        username = request.form.get('username', data)
        #UserModel.verif_user_credentials(data, username, password)
        if UserModel.verif_user_credentials(data, username, password) != None:
            #session['Logged'] = True
            #session['id'] = user['id']
            #session['username'] = user['username']
            flash("Successfully Connected :)")
            print("Work\n")
        else:
            flash("Wrong Username/Password :(")
            print("No\n")
        return render_template("auth/login.html", title="EPyTodo | Connexion :)",
                                   myContent="connect a user")

