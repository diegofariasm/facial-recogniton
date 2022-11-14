from ..models.MAluno import MAluno
from .database import database


class DAluno:
    @staticmethod
    def email_in_db(email):
        exists = MAluno.query.filter_by(email=email).first()
        if exists:
            return True
        else:
            return False

    @staticmethod
    def register_student(model_aluno):

        if not DAluno.email_in_db(model_aluno.email):
            database.session.add(model_aluno)
            database.session.commit()

            return True
        else:
            return False

    @staticmethod
    def get_student(email):
        student = MAluno.query.filter_by(email=email).first()

        if student:
            return student
        else:
            return False
