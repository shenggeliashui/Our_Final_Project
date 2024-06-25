import sys
import os

# 获取当前文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取目标模块所在的目录路径
target_dir = os.path.abspath(os.path.join(current_dir, '..', 'recite'))

# 将目标目录添加到sys.path
sys.path.append(target_dir)

from models import Account, User
from exceptions import CustomException
from mapper import UserMapper
from memorized import get_memorized_num_with_id
from unmemorized import get_unmemorized_num

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
    
    def select_book(self, books):
        per = []
        for i in range(len(books)):
            memorize = get_memorized_num_with_id(books[i].id)
            unmemorize = get_unmemorized_num(books[i].id)
            per.append(memorize / (memorize + unmemorize) * 100)
        book_list = []
        for i in range(len(books)):
            book_list.append({'bookId': books[i].id, 'bookName': books[i].bookId, 'percentage': per[i]})
        return {'books': book_list}
