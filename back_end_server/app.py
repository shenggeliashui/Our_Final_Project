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
    number = get_unmemorized_num()
    return jsonify({'number': number})

@app.route('/api/get-memorized-num', methods=['GET'])
def get_memorized_num_endpoint():
    number = get_memorized_num()
    return jsonify({'number': number})

@app.route('/api/random-get-word-unmemorized', methods=['GET'])
def random_get_word_unmemorized_endpoint():
    word = random_get_word_unmemorized()
    return jsonify({'word': word})

@app.route('/api/get-word-example', methods=['GET'])
def get_word_example_endpoint():
    word = request.args.get('word')
    example = get_word_example(word)
    return jsonify({'example': example})

@app.route('/api/get-word-meaning', methods=['GET'])
def get_word_meaning_endpoint():
    word = request.args.get('word')
    meaning = get_word_meaning(word)
    return jsonify({'meaning': meaning})

@app.route('/api/get-word-phonetic', methods=['GET'])
def get_word_phonetic_endpoint():
    word = request.args.get('word')
    usphone,ukphone = get_word_phonetic(word)
    return jsonify({'usphone': usphone,'ukphone':ukphone})

@app.route('/api/add-memorized-word', methods=['POST'])
def add_memorized_word_endpoint():
    word = request.json.get('word')
    add_memorized_word(word,date.today())
    return '', 204

@app.route('/api/delete-unmemorized-word', methods=['POST'])
def delete_unmemorized_word_endpoint():
    word = request.json.get('word')
    delete_unmemorized_word(word)
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
    app.run(debug=True)
