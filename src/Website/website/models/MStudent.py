from flask_login import UserMixin

from ..dao.database import database

ACESS_LEVELS = {
    'guest': 0,
    'user': 1,
    'admin': 2
}

class MStudent(database.Model, UserMixin):
    __tablename__ = 'student'
    
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255))
    email = database.Column(database.String(255), unique=True)
    password = database.Column(database.String(255))
    acess = database.Column(database.Integer)
    
    
    def __init__(self, name, email, password, acess = ACESS_LEVELS['user']):
        self.name = name
        self.email = email
        self.password = password
        self.acess = acess
    
    def is_allowed(self, acess_level):
        return self.acess >= acess_level
        
