from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.common.cors import configure_cors
from app.exceptions import register_error_handlers

app = Flask(__name__)
app.config.from_object('config.Config')

# 初始化数据库
db = SQLAlchemy(app)

# 配置跨域
configure_cors(app)

# 注册全局异常处理程序
register_error_handlers(app)

# Register blueprints
from app.controllers.uservocab_controller import uservocab_bp
from app.controllers.file_controller import file_bp
from app.controllers.user_controller import user_bp
from app.controllers.web_controller import web_bp

app.register_blueprint(uservocab_bp)
app.register_blueprint(file_bp)
app.register_blueprint(user_bp)
app.register_blueprint(web_bp)

# Import other modules if needed
from app import models, services, exceptions, mappers, common