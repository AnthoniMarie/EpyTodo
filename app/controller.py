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
from app.models import TaskModel
from config import *
import pymysql as sql
import hashlib

class UserController(object):
    def user_add(data):
        username = request.form.get('username', None)
        password_ns = request.form.get('password', None)
        if request.method == "POST" and username and password_ns:
            if UserModel.verif_user_existence(data, username) == None:
                password = hashlib.md5(str(password_ns).encode('utf-8')).hexdigest()
                UserModel.user_add(data, username, password)
                flash("Création de votre compte réussie :)", "success")
            else:
                flash ("Un compte avec ce pseudonyme est déjà occupé :/, copieur", "error")
        elif request.method == "POST":
            flash("Echec de la création de votre compte :(, vérifiez les informations saisies", "error")

        return render_template("auth/register.html", title="EPyTodo | Inscription :)",
                      myContent="register a new user")
    def user_login(data):
        password = hashlib.md5(str(request.form.get('password', data)).encode('utf-8')).hexdigest()
        username = request.form.get('username', data)
        if request.method == "POST" and username and password:
            if UserModel.verif_user_credentials(data, username, password) != None:
                session['user_authenticated'] = True
                session['username'] = username
                return redirect(url_for('route_home'))
                flash("Connexion réussie :)", "success")
            else:
                flash("Pseudonyme/Mot de passe incorrect :(", "error")
        elif request.method == "POST":
            flash("Echec de la connexion, vérifiez les informations saisies", "error")
        return render_template("auth/login.html", title="EPyTodo | Connexion :)",
                                   myContent="connect a user")
    def user_logout(data):
        if session['user_authenticated'] == True:
            del session['user_authenticated']
            flash("Déconnexion réussie", "success")
        return redirect('/')

class TaskController(object):
    def task_list(data):
        title = TaskModel.display_task(data)
        return render_template("tasks/list.html", title="EPyTodo | Liste des tâches",
                           myContent="view all user tasks", task=title)
    def task_add(data):
        title = request.form.get('title', None)
        begin = request.form.get('begin', None)
        end = request.form.get('end', None)
        status = request.form.get('status', None)
        if request.method == "POST" and title and begin and end and status:
            if TaskModel.verif_task_existence(data, title) == None:
                TaskModel.task_add(data, title, begin, end, status)
                flash("Succès de la création de tâche :)", "success")
            else:
                flash("Echec et mat, il y a déja une tâche qui existe", "error")
        elif request.method == "POST":
            flash("Echec de la création de votre tâche :(, vérifiez les informations saisies", "error")
        return redirect('/user/task')
    def task_del(data, task_id):
        TaskModel.task_del(data, task_id)
        flash("Cette tâche a bien été supprimée", "success")
        return redirect('/user/task')


