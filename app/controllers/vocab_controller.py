from flask import Blueprint, request, jsonify
from app.common.result import Result
from app.services.vocab_service import CourseService

course_bp = Blueprint('course', __name__)
course_service = CourseService()

@course_bp.route('/course/selectPage', methods=['GET'])
def select_page():
    page_num = request.args.get('pageNum', default=1, type=int)
    page_size = request.args.get('pageSize', default=5, type=int)
    course = request.args.to_dict()
    page_info = course_service.select_page(page_num, page_size, course)
    return jsonify(Result.success(page_info).to_dict())

@course_bp.route('/course/add', methods=['POST'])
def add_course():
    course = request.get_json()
    course_service.add(course)
    return jsonify(Result.success().to_dict())

@course_bp.route('/course/update', methods=['PUT'])
def update_course():
    course = request.get_json()
    course_service.update_by_id(course)
    return jsonify(Result.success().to_dict())

@course_bp.route('/course/delete/<int:id>', methods=['DELETE'])
def delete_course(id):
    course_service.delete_by_id(id)
    return jsonify(Result.success().to_dict())