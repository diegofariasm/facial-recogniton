from ..dao.DAluno import DAluno
from ..models.MAluno import MAluno


class CAluno:
    @staticmethod
    def register_student(id, name, email, password):
        aluno = MAluno(id, name, email, password)
        DAluno.register_student(aluno)
    @staticmethod    
    def email_used(email):
        used = DAluno.check_email_used(email)

        return used
    @staticmethod
    def id_used(id):
        used = DAluno.check_id_used(id)

        return used