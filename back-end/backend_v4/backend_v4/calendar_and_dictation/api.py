# calendar_and_dictation/api.py
from flask import Flask, request, jsonify
from DictationManager import DictationManager
from word_calendar import get_word_count_and_levels
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# 初始化 DictationManager 实例
dictation_manager = DictationManager()

@app.route('/api/dictation_fetch_random_words', methods=['GET'])
def dictation_fetch_random_words():
    dictation_manager.fetch_random_words()
    if not dictation_manager.words_info:
        return jsonify({'error': 'Failed to fetch random words'}), 500
    
    return jsonify({'message': 'Random words fetched successfully'}), 200

@app.route('/api/dictation_get_current_word', methods=['GET'])
def dictation_get_current_word():
    word = dictation_manager.get_word()
    if not word:
        return jsonify({'error': 'No current word'}), 404
    
    return jsonify({'word': word}), 200

@app.route('/api/dictation_move_to_next_word', methods=['GET'])
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
    current_word = request.args.get('current_word', type=str)
    data = request.get_json()
    user_input = data.get('userInput')
    print(user_input)
    print("ok")
    
    if not user_input:
        return jsonify({'error': 'Missing userInput parameter'}), 400
    match, correct_word = dictation_manager.is_word_match(user_input,current_word)
    print(match)
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
    print(app.url_map)
    app.run(debug=True,port=5000)

