from flask import Blueprint, request, jsonify
from app.common.result import Result
from app.common.role_enum import RoleEnum
from app.services.admin_service import AdminService
from app.services.user_service import UserService

web_bp = Blueprint('web', __name__)
admin_service = AdminService()
user_service = UserService()

@web_bp.route('/', methods=['GET'])
def hello():
    return jsonify(Result.success().to_dict())

@web_bp.route('/login', methods=['POST'])
def login():
    account = request.get_json()
    # 如果考虑增加权限的话 可以使用如下代码
    # role = account.get('role')
    # if role == RoleEnum.ADMIN.name:
    #     db_account = admin_service.login(account)
    # elif role == RoleEnum.STUDENT.name:
    #     db_account = user_service.login(account)
    # else:
    #     return jsonify(Result.error("角色错误").to_dict())
    db_account = user_service.login(account)
    return jsonify(Result.success(db_account).to_dict())

@web_bp.route('/register', methods=['POST'])
def register():
    account = request.get_json()
    if not account.get('username') or not account.get('password'):
        return jsonify(Result.error("账号或密码必须填写！").to_dict())
    user_service.register(account)
    return jsonify(Result.success().to_dict())