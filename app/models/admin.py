from app.models.account import Account

class Admin(Account):
    def __init__(self, id=None, username=None, password=None, name=None):
        super().__init__(username, password, name)
        self.id = id

    def to_dict(self):
        data = super().to_dict()
        data.update({'id': self.id})
        return data