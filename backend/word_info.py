# word_info.py
from db_connection import get_connection
from mysql.connector import Error
import nltk
from nltk.stem import PorterStemmer

def hide_word_in_sentence(sentence, word, stem_word):
    words = nltk.word_tokenize(sentence)
    hidden_sentence = []
    for w in words:
        if PorterStemmer().stem(w) == stem_word:
            hidden_sentence.append('_' * len(w))
        else:
            hidden_sentence.append(w)
    return ' '.join(hidden_sentence)


def get_word_example(word, book_id):
    connection = get_connection()
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            query = """
            SELECT sContent, sCn
            FROM words
            WHERE word = %s AND bookId = %s
            """
            cursor.execute(query, (word, book_id))
            result = cursor.fetchone()

            if result:
                sContent, sCn = result
                stem_word = PorterStemmer().stem(word)
                hidden_sContent = hide_word_in_sentence(sContent, word, stem_word)
                return {'sContent': hidden_sContent, 'sCn': sCn}
    except Error as e:
        print("连接 MySQL 时出错: {}".格式(e))
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def get_word_meaning(word, book_id):
    connection = get_connection()
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            if book_id != 'CET4':
                book_id += '_2'
            query = """
            SELECT pos, tranCn
            FROM words
            WHERE word = %s AND bookId = %s
            """
            cursor.execute(query, (word, book_id))

            word_dict = {}
            for pos, tranCn in cursor:
                if pos in word_dict:
                    word_dict[pos].append(tranCn)
                else:
                    word_dict[pos] = [tranCn]

            return word_dict
    except Error as e:
        print("连接 MySQL 时出错: {}".格式(e))
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def get_word_phonetic(word, book_id):
    connection = get_connection()
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            query = """
            SELECT usphone, ukphone
            FROM words
            WHERE word = %s AND bookId = %s
            """
            cursor.execute(query, (word, book_id))
            phonetics = cursor.fetchone()
            return phonetics if phonetics else (None, None)
    except Error as e:
        print("连接 MySQL 时出错: {}".格式(e))
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
