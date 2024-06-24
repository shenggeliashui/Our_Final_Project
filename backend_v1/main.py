# main.py
from flask import Flask
from dictation_and_calendar.api import app as dictation_and_calendar_app
from information.controller import app as information_app
from recite.app import app as recite_app

app = Flask(__name__)

# 注册各个模块的蓝图
app.register_blueprint(dictation_and_calendar_app, url_prefix='/dictation_and_calendar')
app.register_blueprint(information_app, url_prefix='/information')
app.register_blueprint(recite_app, url_prefix='/recite')

if __name__ == '__main__':
    app.run(debug=True)

