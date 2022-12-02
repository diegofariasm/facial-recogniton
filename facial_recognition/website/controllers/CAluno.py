from flask import flash
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from ..dao.DAluno import DAluno
from ..models.MAluno import MAluno


class CAluno:
    @staticmethod
    def register_student(name, email, password):
        hashed_password = generate_password_hash(password, method="sha256")
        student = MAluno(name, email, hashed_password)

        if DAluno.register_student(student):
            flash("Usuário criado com sucesso", category="sucess")
        else:
            flash("Erro ao criar usuário: email já em uso", category="error")

    def login_student(email, password):
        student = DAluno.get_student(email)

        if student and check_password_hash(student.password, password):
            flash("Usuário logado.", category="sucess")
            login_user(student, remember=True)

            return True

        elif not student:
            flash("Usuário não encontrado", category="error")

        elif not check_password_hash(student.password, password):
            flash("Senha incorreta. Tente novamente.", category="error")
