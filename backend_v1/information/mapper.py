# information/mapper.py
from extensions import db
from .services import User

class UserMapper:
    @staticmethod
    def select_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def insert(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def select_all(user_filter):
        return User.query.filter(
            User.username.like(f"%{user_filter['username']}%"),
            User.name.like(f"%{user_filter['name']}%")
        ).order_by(User.id.desc()).all()

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

