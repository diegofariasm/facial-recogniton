from ..dao.database import database

class MAttendance(database.Model):
    __tablename__ = 'attendance'
    
    id = database.Column(database.Integer, primary_key=True)
    time_done = database.Column(database.String(10))
    student_id = database.Column(database.ForeignKey('student.id'))

    def __init__(self, time, student_id):
        self.time_done = time
        self.student_id = student_id
        

