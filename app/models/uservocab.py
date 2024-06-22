class UserVocab:
    def __init__(self, id=None, username=None, bookname=None, recite=None, forget=None):
        self.id = id
        self.username = username
        self.bookname = bookname
        self.recite = recite
        self.forget = forget

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'bookname': self.bookname,
            'recite': self.recite,
            'forget': self.forget
        }