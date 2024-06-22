from app.models.account import Account

class User(Account):
    def __init__(self, id=None, username=None, password=None, name=None, phone=None, email=None, sex=None, birth=None, avatar=None):
        super().__init__(username, password, name)
        self.id = id
        self.phone = phone
        self.email = email
        self.sex = sex
        self.birth = birth
        self.avatar = avatar

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'id': self.id,
            'phone': self.phone,
            'email': self.email,
            'sex': self.sex,
            'birth': self.birth,
            'avatar': self.avatar
        })
        return data