from flask import Blueprint, render_template, flash
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField, EmailField, PasswordField
from wtforms.validators import DataRequired

from werkzeug.security import generate_password_hash, check_password_hash


from .CAluno import CAluno


auth_routes = Blueprint("auth_routes", __name__)


class formRegistro(FlaskForm):
    id = IntegerField("Número da matrícula", validators=[DataRequired()])
    name = StringField("Nome do estudante", validators=[DataRequired()])
    email = EmailField("Email do estudante", validators=[DataRequired()])
    password = PasswordField("Senha do estudante", validators=[DataRequired()])
    submit = SubmitField("Registrar-se")


@auth_routes.route("/register", methods=["GET", "POST"])
def register():
    id = None
    name = None
    email = None
    password = None
    form = formRegistro()

    if form.validate_on_submit():
        # Pega os valores do formulário
        id = form.id.data
        name = form.name.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method="sha256")

        if CAluno.email_used(email) or CAluno.id_used(id):
            flash("Email em uso!", category="error")
            flash("Número de matrícula já existe!", category="error")
        elif CAluno.id_used(id):
            flash("Número de matrícula já existe!", category="error")
        else:
            CAluno.register_student(id=id, name=name, email=email, password=password)
            flash("Aluno cadastrado com sucesso!", category="sucess")

    return render_template(
        "register.html", id=id, name=name, email=email, password=password, form=form
    )


@auth_routes.route("/sign-in", methods=["GET", "POST"])
def login():
    render_template("login.html")
