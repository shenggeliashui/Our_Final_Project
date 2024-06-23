from app import db

class Account:
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)

    def __init__(self, username=None, email=None, password=None, name=None, role=None):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.role = role

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'name': self.name,
            'role': self.role
        }
    
    def get_password(self):
        return self.password