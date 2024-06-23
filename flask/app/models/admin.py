from app import db
from app.models.account import Account

class Admin(Account):
    __tablename__ = 'admins'  # 这个是数据库表名

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, id=None, username=None, password=None, name=None):
        super().__init__(username, password, name)
        self.id = id

    def to_dict(self):
        data = super().to_dict()
        data.update({'id': self.id})
        return data