from flask import Blueprint, request, jsonify
from app.common.result import Result
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__)
user_service = UserService()

@user_bp.route('/user/add', methods=['POST'])
def add_user():
    user = request.get_json()
    user_service.add(user)
    return jsonify(Result.success().to_dict())

@user_bp.route('/user/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_service.delete_by_id(id)
    return jsonify(Result.success().to_dict())

@user_bp.route('/user/update', methods=['PUT'])
def update_user():
    user = request.get_json()
    user_service.update_by_id(user)
    return jsonify(Result.success().to_dict())

@user_bp.route('/user/selectPage', methods=['GET'])
def select_page():
    page_num = request.args.get('pageNum', default=1, type=int)
    page_size = request.args.get('pageSize', default=10, type=int)
    user = request.args.to_dict()
    page_info = user_service.select_page(page_num, page_size, user)
    return jsonify(Result.success(page_info).to_dict())