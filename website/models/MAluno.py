from flask_login import UserMixin

from ..dao.database import database


class MAluno(database.Model, UserMixin):

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255))
    email = database.Column(database.String(255), unique=True)
    password = database.Column(database.String(64))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
