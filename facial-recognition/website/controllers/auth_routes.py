from flask import Blueprint, render_template, redirect, url_for
from flask_login import logout_user, login_required, current_user
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired


from .CAluno import CAluno


auth_routes = Blueprint("auth_routes", __name__)

class FormRegistro(FlaskForm):
    name = StringField("Nome do estudante:", validators=[DataRequired()])
    email = EmailField("Email do estudante:", validators=[DataRequired()])
    password = PasswordField("Senha do estudante:", validators=[DataRequired()])
    submit = SubmitField("Registrar-se")


@auth_routes.route("/register", methods=["GET", "POST"])
def register():
    name = None
    email = None
    password = None
    form = FormRegistro()

    if form.validate_on_submit():

        name = form.name.data
        email = form.email.data
        password = form.password.data

        CAluno.register_student(name=name, email=email, password=password)
        CAluno.login_student(email, password)
        return redirect(url_for("routes.home"))
    return render_template(
        "register.jinja",
        id=id,
        name=name,
        email=email,
        password=password,
        form=form,
        user=current_user,
    )


class FormLogin(FlaskForm):
    email = EmailField("Email do estudante:", validators=[DataRequired()])
    password = PasswordField("Senha do estudante:", validators=[DataRequired()])
    submit = SubmitField("Entrar")


@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    email = None
    password = None
    form = FormLogin()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if CAluno.login_student(email, password):
            return redirect(url_for("routes.home"))

    return render_template(
        "login.jinja", email=email, password=password, form=form, user=current_user
    )


@auth_routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_routes.login"))
