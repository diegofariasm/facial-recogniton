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
    def get_students_attendance_done():
        present_students = DStudent.get_all_students_attendance_done()
        
        return present_students
    @staticmethod
    def register_student_attendance(id):
        student = DStudent.get_student_from_id(id)
        student_id = student.id
        time_done = date.today()
        if not CStudent.student_attendance_already_done(id):
            attendance = MAttendance(time_done, student_id)
            DAttendance.register_attendance(attendance)
    
    @staticmethod
    def student_attendance_already_done(id):
        time_now = date.today()
        attendance = MAttendance(time_now, id)
        student_attendance = DAttendance.check_attendance_done(attendance)
        
        if student_attendance:
            return True
        else:
            return False
        
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
  