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
        if UserModel.verif_user_existence(data, username) == None:
            print("NEXISTE PAS TA MAMAN LE CHEVAL NOIR DU MONT ROUGE")
        else:
            print("IL EXISTE :)")
        if request.method == "POST" and username and password_ns:
            password = hashlib.sha3_256(str(password_ns).encode('utf-8')).hexdigest()
            UserModel.user_add(data, username, password)
            flash("Création de votre compte réussie :)", "success")
        elif request.method == "POST":
            flash("Echec de la création de votre compte :(, vérifiez les informations saisies", "error")

        return render_template("auth/register.html", title="EPyTodo | Inscription :)",
                      myContent="S'inscrire à l'espace membre EPyTodo")
    def user_login(data):
        username = request.form.get('username', data)
        password = request.form.get('password', data)
        cursor.execute("SELECT * FROM user WHERE username = (%s) AND password = (%s)", (username, password,))
        user = cursor.fetchone()
        if (user):
            session['Logged'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            flash("Successfully Connected :)")
            print("Work\n")
        else:
            flash("Wrong Username/Password :(")
            print("No\n")
        return render_template("auth/login.html", title="EPyTodo | Connexion :)",
                                   myContent="Connexion à l'espace membre EPyTodo")

