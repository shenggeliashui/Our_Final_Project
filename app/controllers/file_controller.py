# 头像上传
from flask import Blueprint, request, jsonify, send_file
from app.common.result import Result
import os
import time
from werkzeug.utils import secure_filename

file_bp = Blueprint('files', __name__)
ROOT_PATH = os.path.join(os.getcwd(), 'files')

@file_bp.route('/files/upload', methods=['POST'])
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

@file_bp.route('/files/download', methods=['GET'])
def download():
    file_name = request.args.get('fileName')
    file_path = os.path.join(ROOT_PATH, file_name)
    return send_file(file_path, as_attachment=True)