from app.models.uservocab import UserVocab
from app import db

class UserVocabMapper:
    @staticmethod
    def select_all(uservocab_filter):
        return UserVocab.query.filter(
            UserVocab.username.like(f"%{uservocab_filter['username']}%"),
            UserVocab.bookname.like(f"%{uservocab_filter['bookname']}%")
        ).order_by(UserVocab.id.asc()).all()

    @staticmethod
    def insert(uservocab):
        db.session.add(uservocab)
        db.session.commit()

    @staticmethod
    def update_by_id(uservocab):
        db.session.merge(uservocab)
        db.session.commit()

    @staticmethod
    def delete_by_id(uservocab_id):
        uservocab = UserVocab.query.get(uservocab_id)
        if uservocab:
            db.session.delete(uservocab)
            db.session.commit()