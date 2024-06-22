class Account:
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