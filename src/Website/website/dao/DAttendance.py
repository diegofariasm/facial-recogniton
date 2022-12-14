from ..models.MAttendance import MAttendance
from .database import database
from datetime import date

class DAttendance:
    
    @staticmethod
    def register_attendance(MAttendance):
                
        if not DAttendance.check_attendance_done(MAttendance):
            database.session.add(MAttendance)
            database.session.commit()
            return True
        else:
            return False
    
    @staticmethod
    def check_attendance_done(MAttendance):
        time_done = MAttendance.time_done
        student_id = MAttendance.student_id
        attendance = MAttendance.query.filter_by(time_done=time_done, id=student_id).first()
        
        if attendance:
            return True
        else:
            return False
        