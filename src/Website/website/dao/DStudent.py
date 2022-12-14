from ..models.MStudent import MStudent
from ..models.MAttendance import MAttendance
from .database import database
from datetime import date


class DStudent:
    @staticmethod
    def get_all_students_attendance_done():
        students_present = MStudent.query\
        .join(MAttendance, MAttendance.student_id==MStudent.id and MAttendance.time_done == date.today())
        
        return students_present
    @staticmethod
    def get_all_students():
        students = MStudent.query.all()
        
        return students
    
    @staticmethod
    def email_in_db(email):
        exists = MStudent.query.filter_by(email=email).first()
        if exists:
            return True
        else:
            return False
    
    @staticmethod
    def register_student(model_aluno):

        if not DStudent.email_in_db(model_aluno.email):
            database.session.add(model_aluno)
            database.session.commit()

            return True
        else:
            return False

    @staticmethod
    def get_student(email):
        student = MStudent.query.filter_by(email=email).first()

        if student:
            return student
        else:
            return False
    @staticmethod
    def get_student_from_id(id):
        student = MStudent.query.filter_by(id = id).first()

        if student:
            return student
        else:
            return False
    
