from ..models.MAluno import MAluno
from .database import database


class DAluno:
    nome = ""
    email = ""
    password = ""

    def __init__(self, id, name, email, password):
        self.id = id
        self.nome = name
        self.email = email
        self.password = password

    @staticmethod
    def register_student(MAluno):
        database.session.add(MAluno)
        database.session.commit()

    @staticmethod
    def check_email_used(email):
        email_aluno = MAluno.query.filter_by(email=email).first()
        if email_aluno:
            return True
        else:
            return False

    def check_id_used(id):
        id_aluno = MAluno.query.filter_by(id=id).first()
        if id_aluno:
            return True
        else:
            return False
