from flask import Blueprint, request, jsonify
from app.common.result import Result
from app.services.uservocab_service import UserVocabService

uservocab_bp = Blueprint('uservocab', __name__)
uservocab_service = UserVocabService()

@uservocab_bp.route('/uservocab/selectPage', methods=['GET'])
def select_page():
    page_num = request.args.get('pageNum', default=1, type=int)
    page_size = request.args.get('pageSize', default=5, type=int)
    uservocab = request.args.to_dict()
    page_info = uservocab_service.select_page(page_num, page_size, uservocab)
    return jsonify(Result.success(page_info).to_dict())

@uservocab_bp.route('/uservocab/add', methods=['POST'])
def add_uservocab():
    uservocab = request.get_json()
    uservocab_service.add(uservocab)
    return jsonify(Result.success().to_dict())

@uservocab_bp.route('/uservocab/update', methods=['PUT'])
def update_uservocab():
    uservocab = request.get_json()
    uservocab_service.update_by_id(uservocab)
    return jsonify(Result.success().to_dict())

@uservocab_bp.route('/uservocab/delete/<int:id>', methods=['DELETE'])
def delete_uservocab(id):
    uservocab_service.delete_by_id(id)
    return jsonify(Result.success().to_dict())