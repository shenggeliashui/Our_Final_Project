from db_connection import get_connection
from mysql.connector import Error
import nltk
from nltk.stem import PorterStemmer

# 指定 NLTK 数据路径
nltk.data.path.append('./nltk_data')

class DictationManager:
    def __init__(self):
        self.words_info = []
        self.current_index = 0

    def fetch_random_words(self, book_id):
        connection = get_connection()
        try:
            if connection:
                cursor = connection.cursor()
                
                # 从 test_table 中随机抽取 10 个单词
                query = """
                SELECT word
                FROM test_table
                WHERE bookId = %s
                ORDER BY RAND()
                LIMIT 10
                """
                cursor.execute(query, (book_id,))
                random_words = cursor.fetchall()

                # 查询这些单词在 words 表中的全部信息
                for word in random_words:
                    query = """
                    SELECT id, word, bookId, tranCn, pos, usphone, ukphone, sContent, sCn
                    FROM words
                    WHERE word = %s AND bookId = %s
                    """
                    cursor.execute(query, (word[0], book_id))
                    word_info = cursor.fetchone()
                    if word_info:
                        self.words_info.append(word_info)
        except Error as e:
            print("连接 MySQL 时出错: {}".format(e))
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    def get_current_word(self):
        if self.current_index < len(self.words_info):
            return self.words_info[self.current_index]
        return None

    def move_to_next_word(self):
        self.current_index += 1
        if self.current_index >= len(self.words_info):
            self.words_info = []
            self.current_index = 0
            print("没有更多的单词")
            return False
        return True

    def get_phonetics(self):
        current_word = self.get_current_word()
        if current_word:
            _, _, _, _, _, usphone, ukphone, _, _ = current_word
            return usphone, ukphone
        return None, None

    def get_word(self):
        current_word = self.get_current_word()
        if current_word:
            _, word, _, _, _, _, _, _, _ = current_word
            return word
        return None

    def get_pos_and_tran(self):
        current_word = self.get_current_word()
        if current_word:
            _, _, _, tranCn, pos, _, _, _, _ = current_word
            return {pos: [tranCn]}
        return {}

    def get_example(self):
        current_word = self.get_current_word()
        if current_word:
            _, word, _, _, _, _, _, sContent, sCn = current_word
            stem_word = PorterStemmer().stem(word)
            hidden_sContent = self.hide_word_in_sentence(sContent, word, stem_word)
            return {"sContent": hidden_sContent, "sCn": sCn}
        return {}

    def is_word_match(self, input_word):
        """
        判断输入字符串是否与当前单词相同。
        """
        current_word = self.get_word()
        if current_word:
            if current_word.lower() == input_word.lower():
                return True, None
            else:
                return False, current_word
        return False, None

    @staticmethod
    def hide_word_in_sentence(sentence, word, stem_word):
        words = nltk.word_tokenize(sentence)
        hidden_sentence = []
        for w in words:
            if PorterStemmer().stem(w) == stem_word:
                hidden_sentence.append('_' * len(w))
            else:
                hidden_sentence.append(w)
        return ' '.join(hidden_sentence)

    def __del__(self):
        print("DictationManager 实例已销毁")

