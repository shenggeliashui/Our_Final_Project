from app.models.admin import Admin
from app import db

class AdminMapper:
    @staticmethod
    def select_by_username(username):
        return Admin.query.filter_by(username=username).first()