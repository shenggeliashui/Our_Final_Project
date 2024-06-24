import logging
from flask import Flask, jsonify
from .common import Result

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
    
class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def get_msg(self):
        return self.msg
