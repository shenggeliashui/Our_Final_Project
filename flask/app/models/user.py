from app import db
from app.models.account import Account

class User(Account):
    __tablename__ = 'users'  # 数据库表名

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sex = db.Column(db.String(10), nullable=True)
    birth = db.Column(db.Date, nullable=True)
    avatar = db.Column(db.String(256), nullable=True)
    cur_book = db.Column(db.String(256), nullable=True)

    def __init__(self, id=None, username=None, password=None, name=None, phone=None, email=None, sex=None, birth=None, avatar=None, cur_book=None):
        super().__init__(username, password, name)
        self.id = id
        self.phone = phone
        self.email = email
        self.sex = sex
        self.birth = birth
        self.avatar = avatar
        self.cur_book = cur_book

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'id': self.id,
            'phone': self.phone,
            'email': self.email,
            'sex': self.sex,
            'birth': self.birth,
            'avatar': self.avatar,
            'cur_book': self.cur_book
        })
        return data