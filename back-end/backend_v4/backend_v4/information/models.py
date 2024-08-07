from main import db
from werkzeug.security import generate_password_hash, check_password_hash

class Account:
    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'email': self.email
        }
    
    def get_password(self):
        return self.password

class User(db.Model):
    __tablename__ = 'user'  # 数据库表名

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    cur_book = db.Column(db.String(256), nullable=False)
    username = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(256), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    birth = db.Column(db.Date, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sex = db.Column(db.String(256), nullable=True)
    avatar = db.Column(db.String(256), nullable=True)

    def __init__(self, id=None, cur_book=None, username=None, password=None, name=None, phone=None, birth=None, email=None, sex=None, avatar=None):
        super().__init__(username, password, name)
        self.id = id
        self.cur_book = cur_book
        self.username = username
        self.password = password
        self.name = name
        self.phone = phone
        self.birth = birth
        self.email = email
        self.sex = sex
        self.avatar = avatar

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'id': self.id,
            'cur_book': self.cur_book,
            'username': self.username,
            'password': self.password,
            'name': self.name,
            'phone': self.phone,
            'birth': self.birth,
            'email': self.email,
            'sex': self.sex,
            'avatar': self.avatar
        })
        return data
    
class Word(db.Model):
    __tablename__ = 'words'  # 数据库表名

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    word = db.Column(db.String(256), nullable=False)
    bookId = db.Column(db.String(50), nullable=False)
    tranCn = db.Column(db.String(256), nullable=False)
    pos = db.Column(db.String(50), nullable=False)
    usphone = db.Column(db.String(256), nullable=False)
    ukphone = db.Column(db.String(256), nullable=False)
    sContent = db.Column(db.String(256), nullable=False)
    sCn = db.Column(db.String(256), nullable=False)

    def __init__(self, id=None, word=None, bookId=None, tranCn=None, pos=None, usphone=None, ukphone=None, sContent=None, sCn=None):
        super().__init__()
        self.id = id
        self.word = word
        self.bookId = bookId
        self.tranCn = tranCn
        self.pos = pos
        self.usphone = usphone
        self.ukphone = ukphone
        self.sContent = sContent
        self.sCn = sCn

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'id': self.id,
            'word': self.word,
            'bookId': self.bookId,
            'tranCn': self.tranCn,
            'pos': self.pos,
            'usphone': self.usphone,
            'ukphone': self.ukphone,
            'sContent': self.sContent,
            'sCn': self.sCn
        })
        return data