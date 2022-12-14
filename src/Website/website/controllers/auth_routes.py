from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import logout_user, login_required, current_user
from flask_wtf import FlaskForm
from flask_wtf.file import  FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

from wtforms import StringField, SubmitField, EmailField, PasswordField, FileField
from wtforms.validators import DataRequired


from .CStudent import CStudent
from .CPicture import CPicture

import os
auth_routes = Blueprint("auth_routes", __name__)

class FormRegistro(FlaskForm):
    name = StringField("Nome do estudante:", validators=[DataRequired()])
    email = EmailField("Email do estudante:", validators=[DataRequired()])
    password = PasswordField("Senha do estudante:", validators=[DataRequired()])
    student_photo = FileField("Foto do estudante", validators=[FileRequired()])
    
    submit = SubmitField("Registrar-se")


@auth_routes.route("/register", methods=["GET", "POST"])
def register():
    form = FormRegistro()
    name = None
    email = None
    password = None
    student_photo = None
    

    if form.validate_on_submit():

        name = form.name.data
        email = form.email.data
        password = form.password.data
        student_photo = form.student_photo.data
        filename = secure_filename(student_photo.filename)
        CStudent.register_student(name=name, email=email, password=password)
        CStudent.login_student(email, password)
        
        photo_data = student_photo.read()
        CPicture.save_photo(file_name = filename, file_data=photo_data, student_id=current_user.id)
        

        return redirect(url_for("routes.home"))
    
    return render_template(
        "register.html",
        id=id,
        name=name,
        email=email,
        password=password,
        form=form,
        student_photo=student_photo,
        user=current_user,
    )


class FormLogin(FlaskForm):
    email = EmailField("Email do estudante:", validators=[DataRequired()])
    password = PasswordField("Senha do estudante:", validators=[DataRequired()])
    submit = SubmitField("Entrar", validators=[FileRequired()])


@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    email = None
    password = None
    form = FormLogin()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if CStudent.login_student(email, password):
            return redirect(url_for("routes.home"))

    return render_template(
        "login.html", 
        email=email, 
        password=password, 
        form=form, 
        user=current_user
    )


@auth_routes.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("auth_routes.login"))
