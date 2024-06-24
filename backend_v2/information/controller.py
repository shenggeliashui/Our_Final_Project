from flask import Flask, request, jsonify, send_file, session
from flask_cors import CORS
from main import app, db
from services import UserService
from models import User
import os
import time
from werkzeug.utils import secure_filename

CORS(app)
user_service = UserService()
ROOT_PATH = os.path.join(os.getcwd(), 'files')

# 用户管理和文件上传 API 路由
@app.route('/api', methods=['GET'])
def api_hello():
    return jsonify(Result.success().to_dict())

@app.route('/api/login', methods=['POST'])
def login():
    account = request.get_json()
    db_account = user_service.login(account)
    session['user_id'] = db_account.username
    return jsonify(Result.success(db_account).to_dict())

@app.route('/api/register', methods=['POST'])
def register():
    account = request.get_json()
    if not account.get('username') or not account.get('password'):
        return jsonify(Result.error("账号或密码必须填写！").to_dict())
    user_service.register(account)
    return jsonify(Result.success().to_dict())

@app.route('/api/profile', methods=['GET'])
def profile():
    if 'user_id' not in session:
        return jsonify(Result.error("user not logged in").to_dict())

    user_id = session['user_id']
    user = User.query.get(user_id)

    if user:
        return jsonify(Result.success().to_dict())
    else:
        return jsonify(Result.error("user not found").to_dict())

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

@app.route('/api/userAdd', methods=['POST'])
def add_user():
    user = request.get_json()
    if not user.get('username') or not user.get('password'):
        return jsonify(Result.error("账号或密码必须填写！").to_dict())
    user_service.add(user)
    return jsonify(Result.success().to_dict())

@app.route('/api/userDelete/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_service.delete_by_id(id)
    return jsonify(Result.success().to_dict())

@app.route('/api/userUpdateInformation', methods=['PUT'])
def update_user_information():
    user = request.get_json()
    user_service.update_by_id(user)
    return jsonify(Result.success().to_dict())

@app.route('/api/userUpdateBookId', methods=['PUT'])
def update_user_bookId():
    user = request.get_json()
    if not user.get('cur_book'):
        return jsonify(Result.error("您未选择词库！").to_dict())
    user_service.update_by_id(user)
    return jsonify(Result.success().to_dict())

@app.route('/api/userSelectPage', methods=['GET'])
def select_page():
    user = request.args.to_dict()
    page_info = user_service.select_page(user)
    return jsonify(Result.success(page_info).to_dict())

if __name__ == '__main__':
    app.run(debug=True, port=5002)

