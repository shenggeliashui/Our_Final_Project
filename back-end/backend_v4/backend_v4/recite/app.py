# recite/app.py
# 在 recite/app.py 中
import sys
import os

# 获取当前脚本的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取目标模块的目录并添加到 sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, "calendar_and_dictation"))
sys.path.append(parent_dir)

from db_connection import get_book_id
from flask import Flask, jsonify, request
from flask_cors import CORS
from memorized import get_memorized_num, add_memorized_word
from unmemorized import get_unmemorized_num, random_get_word_unmemorized, delete_unmemorized_word, transfer_to_unmemorized, clear_unmemorized_vocabulary
from vocabulary import get_word_example, get_word_meaning, get_word_phonetic
from datetime import date

app = Flask(__name__)
CORS(app)  # 允许所有域名的跨域请求

# 测试函数
# @app.route('/api/write-test-file', methods=['GET'])
# def change_testfile_endpoint():
#     name = request.args.get('name')
#     change_testfile(name)
#     return "good"

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Flask!'})

# 实用函数
@app.route('/api/get-unmemorized-num', methods=['GET'])
def get_unmemorized_num_endpoint():
    book_id = get_book_id()
    number = get_unmemorized_num(book_id)
    return jsonify({'number': number})

@app.route('/api/get-memorized-num', methods=['GET'])
def get_memorized_num_endpoint():
    number = get_memorized_num()
    return jsonify({'number': number})

@app.route('/api/random-get-word-unmemorized', methods=['GET'])
def random_get_word_unmemorized_endpoint():
    book_id = get_book_id()
    word = random_get_word_unmemorized(book_id)
    return jsonify({'word': word})

@app.route('/api/get-word-example', methods=['GET'])
def get_word_example_endpoint():
    book_id = get_book_id()
    word = request.args.get('word')
    example = get_word_example(word,book_id)
    return jsonify({'example': example})

@app.route('/api/get-word-meaning', methods=['GET'])
def get_word_meaning_endpoint():
    book_id = get_book_id()
    word = request.args.get('word')
    meaning = get_word_meaning(word,book_id)
    return jsonify({'meaning': meaning})

@app.route('/api/get-word-phonetic', methods=['GET'])
def get_word_phonetic_endpoint():
    word = request.args.get('word')
    usphone,ukphone = get_word_phonetic(word)
    return jsonify({'usphone': usphone,'ukphone':ukphone})

@app.route('/api/add-memorized-word', methods=['POST'])
def add_memorized_word_endpoint():
    word = request.json.get('word')
    book_id = get_book_id()
    add_memorized_word(word, book_id, date.today())
    return '', 204

@app.route('/api/delete-unmemorized-word', methods=['POST'])
def delete_unmemorized_word_endpoint():
    word = request.json.get('word')
    book_id = get_book_id()
    delete_unmemorized_word(word, book_id)
    return '', 204

@app.route('/api/transfer-to-unmemorized', methods=['POST'])
def transfer_to_unmemorized_endpoint():
    word = request.json.get('word')
    transfer_to_unmemorized(word)
    return '', 204

@app.route('/api/clear-unmemorized-vocabulary', methods=['POST'])
def clear_unmemorized_vocabulary_endpoint():
    clear_unmemorized_vocabulary()
    return '', 204
    
if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, port=5001)

