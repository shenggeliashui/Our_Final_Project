from flask import request, jsonify, send_file
from common import Result
from services import UserService
import os
import time
from werkzeug.utils import secure_filename
from main import app

# 首页页面
user_service = UserService()
@app.route('/api', methods=['GET'])
def hello():
    return jsonify(Result.success().to_dict())

# 登录页面
@app.route('/api/login', methods=['POST'])
def login():
    account = request.get_json()
    db_account = user_service.login(account)
    return jsonify(Result.success(db_account).to_dict())

# 注册页面
@app.route('/api/register', methods=['POST'])
def register():
    account = request.get_json()
    if not account.get('username') or not account.get('password'):
        return jsonify(Result.error("账号或密码必须填写！").to_dict())
    user_service.register(account)
    return jsonify(Result.success().to_dict())

ROOT_PATH = os.path.join(os.getcwd(), 'files')
@app.route('/api/files/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify(Result.error("No file part").to_dict())
    file = request.files['file']
    if file.filename == '':
        return jsonify(Result.error("No selected file").to_dict())

    if file:
        filename = secure_filename(file.filename)
        timestamp = int(time.time())
        final_filename = f"{timestamp}_{filename}"
        final_file_path = os.path.join(ROOT_PATH, final_filename)
        os.makedirs(ROOT_PATH, exist_ok=True)
        file.save(final_file_path)
        url = f"http://{request.host}/files/download?fileName={final_filename}"
        return jsonify(Result.success(url).to_dict())

@app.route('/api/files/download', methods=['GET'])
def download():
    file_name = request.args.get('fileName')
    file_path = os.path.join(ROOT_PATH, file_name)
    return send_file(file_path, as_attachment=True)

user_service = UserService()
@app.route('/api/user/add', methods=['POST'])
def add_user():
    user = request.get_json()
    user_service.add(user)
    return jsonify(Result.success().to_dict())

@app.route('/api/user/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_service.delete_by_id(id)
    return jsonify(Result.success().to_dict())

@app.route('/api/user/update', methods=['PUT'])
def update_user():
    user = request.get_json()
    user_service.update_by_id(user)
    return jsonify(Result.success().to_dict())

@app.route('/api/user/selectPage', methods=['GET'])
def select_page():
    page_num = request.args.get('pageNum', default=1, type=int)
    page_size = request.args.get('pageSize', default=10, type=int)
    user = request.args.to_dict()
    page_info = user_service.select_page(page_num, page_size, user)
    return jsonify(Result.success(page_info).to_dict())