from flask import flash
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from ..dao.DStudent import DStudent
from ..models.MStudent import MStudent
from ..models.MAttendance import MAttendance
from ..dao.DAttendance import DAttendance
from datetime import date


class CStudent:
    @staticmethod
    def get_all_students():
        students = DStudent.get_all_students()
        
        return students
        
    @staticmethod
    def register_student_attendance(id):
        student = MStudent.query.filter_by(id=id).first()
        student_id = student.id
        time_done = date.today()
        
        attendance = MAttendance(time_done, student_id)
        DAttendance.register_attendance(attendance)
        
        
    @staticmethod
    def register_student(name, email, password):
        hashed_password = generate_password_hash(password, method="sha256")
        student = MStudent(name, email, hashed_password)

        if DStudent.register_student(student):
            flash("Usuário criado com sucesso", category="sucess")
        else:
            flash("Erro ao criar usuário: email já em uso", category="error")

    def login_student(email, password):
        student = DStudent.get_student(email)

        if student and check_password_hash(student.password, password):
            flash("Usuário logado.", category="sucess")
            login_user(student, remember=True)

            return True

        elif not student:
            flash("Usuário não encontrado", category="error")

        elif not check_password_hash(student.password, password):
            flash("Senha incorreta. Tente novamente.", category="error")
  