from .models import Account, User
from .exceptions import CustomException
from .mapper import UserMapper

class UserService:
    def __init__(self):
        self.user_mapper = UserMapper()

    def login(self, account: Account) -> Account:
        db_user = self.user_mapper.select_by_username(account.username)
        if db_user is None or account.get_password() != db_user.get_password():
            raise CustomException("账号或密码错误")
        return db_user

    def register(self, account: Account):
        user = User(
            username=account.username,
            email=account.email,
            password=account.password,
        )
        self.add(user)

    def add(self, user: User):
        db_user = self.user_mapper.select_by_username(user.username)
        if db_user is not None:
            raise CustomException("该账号已存在！")
        if not user.name:
            user.name = user.username
        self.user_mapper.insert(user)

    def delete_by_id(self, user_id: int):
        self.user_mapper.delete_by_id(user_id)

    def update_by_id(self, user: User):
        self.user_mapper.update_by_id(user)

    def select_page(self, user_filter: dict):
        return self.user_mapper.select_all(user_filter).items
