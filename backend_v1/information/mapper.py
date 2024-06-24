from services import User
from main import db

class UserMapper:
    @staticmethod
    def select_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def insert(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def delete_by_id(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()

    @staticmethod
    def update_by_id(user):
        db.session.merge(user)
        db.session.commit()