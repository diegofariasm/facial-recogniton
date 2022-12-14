from ..dao.database import database

class MPicture(database.Model):
    __tablename__ = 'photo'
    id = database.Column(database.Integer, primary_key = True)
    file_name = database.Column(database.String(255))
    file_data = database.Column(database.LargeBinary)
    student_id = database.Column(database.ForeignKey('student.id'))
    
    def __init__(self, file_name, file_data, student_id) -> None:
        self.file_name = file_name
        self.file_data = file_data
        self.student_id = student_id
    