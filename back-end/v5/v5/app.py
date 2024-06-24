from flask import Flask, jsonify, request
from flask_cors import CORS

from recite.memorized import get_memorized_num, add_memorized_word
from recite.unmemorized import get_unmemorized_num, random_get_word_unmemorized, delete_unmemorized_word, transfer_to_unmemorized, clear_unmemorized_vocabulary
from recite.vocabulary import get_word_example, get_word_meaning, get_word_phonetic

from datetime import date

from dictation.DictationManager import DictationManager
from my_calendar.word_calendar import get_word_count_and_levels

app = Flask(__name__)
CORS(app)  # 允许所有域名的跨域请求

# 初始化 DictationManager 实例
dictation_manager = DictationManager()

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
    usphone, ukphone = get_word_phonetic(word)
    return jsonify({'usphone': usphone, 'ukphone': ukphone})

@app.route('/api/add-memorized-word', methods=['POST'])
def add_memorized_word_endpoint():
    word = request.json.get('word')
    add_memorized_word(word, date.today())
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

@app.route('/api/dictation_fetch_random_words', methods=['GET'])
def dictation_fetch_random_words():
    book_id = request.args.get('book_id')
    if not book_id:
        return jsonify({'error': 'Missing book_id parameter'}), 400
    
    dictation_manager.fetch_random_words(book_id)
    if not dictation_manager.words_info:
        return jsonify({'error': 'Failed to fetch random words'}), 500
    
    return jsonify({'message': 'Random words fetched successfully'}), 200

@app.route('/api/dictation_get_current_word', methods=['GET'])
def dictation_get_current_word():
    current_word = dictation_manager.get_current_word()
    if not current_word:
        return jsonify({'error': 'No current word'}), 404
    
    return jsonify({
        'id': current_word[0],
        'word': current_word[1],
        'bookId': current_word[2],
        'tranCn': current_word[3],
        'pos': current_word[4],
        'usphone': current_word[5],
        'ukphone': current_word[6],
        'sContent': current_word[7],
        'sCn': current_word[8]
    }), 200

@app.route('/api/dictation_move_to_next_word', methods=['POST'])
def dictation_move_to_next_word():
    if not dictation_manager.move_to_next_word():
        return jsonify({'message': 'No more words'}), 200
    
    return jsonify({'message': 'Moved to next word'}), 200

@app.route('/api/dictation_get_phonetics', methods=['GET'])
def dictation_get_phonetics():
    usphone, ukphone = dictation_manager.get_phonetics()
    return jsonify({'usphone': usphone, 'ukphone': ukphone}), 200

@app.route('/api/dictation_get_word', methods=['GET'])
def dictation_get_word():
    word = dictation_manager.get_word()
    if not word:
        return jsonify({'error': 'No current word'}), 404
    
    return jsonify({'word': word}), 200

@app.route('/api/dictation_get_pos_and_tran', methods=['GET'])
def dictation_get_pos_and_tran():
    pos_and_tran = dictation_manager.get_pos_and_tran()
    return jsonify(pos_and_tran), 200

@app.route('/api/dictation_get_example', methods=['GET'])
def dictation_get_example():
    example = dictation_manager.get_example()
    return jsonify(example), 200

@app.route('/api/dictation_is_word_match', methods=['POST'])
def dictation_is_word_match():
    data = request.get_json()
    user_input = data.get('userInput')
    
    if not user_input:
        return jsonify({'error': 'Missing userInput parameter'}), 400
    
    match, correct_word = dictation_manager.is_word_match(user_input)
    if match:
        return jsonify({'match': True}), 200
    else:
        return jsonify({'match': False, 'correct_word': correct_word}), 200

@app.route('/api/get_word_count', methods=['GET'])
def get_word_count_endpoint():
    year = request.args.get('year', type=int)
    month = request.args.get('month', type=int)

    if year is None or month is None:
        return jsonify({"error": "Year and month parameters are required"}), 400

    word_count_array = get_word_count_and_levels(year, month)
    if word_count_array is None:
        return jsonify({"error": "Error fetching word count"}), 500

    return jsonify(word_count_array)

if __name__ == '__main__':
    app.run(debug=True)

