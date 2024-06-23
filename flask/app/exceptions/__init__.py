# 暂时不用改该文件目录下的
import logging
from flask import Flask, jsonify
from app.common.result import Result
from app.exceptions.custom_exceptions import CustomException

logger = logging.getLogger(__name__)

def register_error_handlers(app: Flask):
    @app.errorhandler(Exception)
    def handle_exception(e):
        logger.error(f"Exception: {e}")
        response = Result.error().to_dict()
        return jsonify(response), 500

    @app.errorhandler(CustomException)
    def handle_custom_exception(e):
        logger.error(f"CustomException: {e.get_msg()}")
        response = Result.error(e.get_msg()).to_dict()
        return jsonify(response), 400
    
# 在这里可以定义其他异常处理程序