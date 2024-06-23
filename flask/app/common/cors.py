from flask import Flask
from flask_cors import CORS

def configure_cors(app: Flask):
    # 配置跨域
    CORS(app, resources={r"/*": {"origins": "*"}})