# backend.py
import sys
from os.path import abspath, dirname

# 确保项目根目录在 PYTHONPATH 中
sys.path.append(dirname(abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from extensions import db
from dictation_and_calendar.api import api_blueprint as dictation_and_calendar_blueprint
from information.controller import controller_blueprint as information_blueprint
from recite.app import recite_blueprint

app = Flask(__name__)
CORS(app)

# 正确配置数据库连接信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://correct_username:correct_password@localhost:3306/wordapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 注册各个模块的蓝图
app.register_blueprint(dictation_and_calendar_blueprint, url_prefix='/dictation_and_calendar')
app.register_blueprint(information_blueprint, url_prefix='/information')
app.register_blueprint(recite_blueprint, url_prefix='/recite')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

