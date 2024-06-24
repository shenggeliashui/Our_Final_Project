from flask import Flask, jsonify, request
from flask_cors import CORS
from random_words import get_random_words_info, get_current_word, update_cursor
from word_info import get_word_example, get_word_meaning, get_word_phonetic
from word_calendar import get_word_count_and_levels

app = Flask(__name__)
CORS(app)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Flask!'})

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

@app.route('/api/get_random_words_info', methods=['GET'])
def get_random_words_info_endpoint():
    book_id = request.args.get('book_id')
    if not book_id:
        return jsonify({"error": "Book ID is required"}), 400

    success = get_random_words_info(book_id)
    if not success:
        return jsonify({"error": "Error fetching words info"}), 500

    return jsonify({"message": "Words info stored successfully"})

@app.route('/api/get_word_example', methods=['GET'])
def get_word_example_endpoint():
    current_word = get_current_word()
    if not current_word:
        return jsonify({"error": "No current word found"}), 500
    
    word, book_id = current_word
    example = get_word_example(word, book_id)
    if example is None:
        return jsonify({"error": "Error fetching word example"}), 500

    return jsonify({'example': example})

@app.route('/api/get_word_meaning', methods=['GET'])
def get_word_meaning_endpoint():
    current_word = get_current_word()
    if not current_word:
        return jsonify({"error": "No current word found"}), 500
    
    word, book_id = current_word
    meaning = get_word_meaning(word, book_id)
    if meaning is None:
        return jsonify({"error": "Error fetching word meaning"}), 500

    return jsonify({'meaning': meaning})

@app.route('/api/get_word_phonetic', methods=['GET'])
def get_word_phonetic_endpoint():
    current_word = get_current_word()
    if not current_word:
        return jsonify({"error": "No current word found"}), 500
    
    word, book_id = current_word
    phonetics = get_word_phonetic(word, book_id)
    if phonetics is None:
        return jsonify({"error": "Error fetching word phonetic"}), 500

    return jsonify({'usphone': phonetics[0], 'ukphone': phonetics[1]})

@app.route('/api/check_word', methods=['POST'])
def check_word_endpoint():
    data = request.json
    user_input = data.get('userInput')

    current_word = get_current_word()
    if not current_word:
        return jsonify({"error": "No current word found"}), 500

    word, book_id = current_word
    correct = user_input == word

    next_word = update_cursor()

    return jsonify({'correct': correct, 'next_word': next_word})

if __name__ == '__main__':
    app.run(debug=True)

