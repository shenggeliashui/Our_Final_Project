from app.models.account import Account
from app.models.admin import Admin
from app.exceptions.custom_exceptions import CustomException
from app.mappers.admin_mapper import AdminMapper

class AdminService:
    def __init__(self):
        self.admin_mapper = AdminMapper()

    def login(self, account: Account) -> Account:
        db_admin = self.admin_mapper.select_by_username(account.username)
        if db_admin is None or not account.get_password() != db_admin.get_password():
            raise CustomException("账号或密码错误")
        return db_admin