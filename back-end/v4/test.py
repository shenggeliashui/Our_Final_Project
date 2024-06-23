import os
import random
from datetime import date
import memorized
import unmemorized
import vocabulary
import pymysql
from main import create_database,initialize_tables
from main import main as initialize

def main():
    book_id=input()
    initialize(book_id)

    # # 给未背词表导入所需要学习的书本单词
    vocabulary.change_book(book_id)
    # 获取未背单词表中单词数量
    word_count = unmemorized.get_unmemorized_num()
    print(word_count)

    # 从未背词库中随机抽取并返回单词
    random_word = unmemorized.random_get_word_unmemorized()
    if random_word:
        print(f"Random word from unmemoried vocabulary: {random_word}")
    else:
        print("No words in unmemoried vocabulary.")

    # 删除未背词库中的指定单词
    unmemorized.delete_unmemorized_word(random_word)

    # 增加单词到已背单词表中
    memorized.add_memorized_word(random_word, date.today())

    # 获取已背单词表中单词数量
    word_count = memorized.get_memorized_num()
    if word_count is not None:
        print(f"Total number of words in the vocabulary: {word_count}")
    else:
        print("Failed to retrieve word count.")

    # 根据单词从完整词库中获取并返回音标
    usphone, ukphone = vocabulary.get_word_phonetic(random_word)
    print(f"US Phonetics: {usphone}")
    print(f"UK Phonetics: {ukphone}")

    
    # 根据单词从完整词库中获取并返回字典（这个暂时无法运行，因为完整词库那边有点问题，后续会修改）
    word_meanings = vocabulary.get_word_meaning(random_word)
    print(word_meanings)
    

    # 根据单词从完整词库中获取例句字典{英文例句,中文翻译}
    word_examples = vocabulary.get_word_example(random_word)
    print(word_examples)

    # 清空整个数据库
    # vocabulary.clear_Memorized_Database()


if __name__ == "__main__":
    main()   # 其中为函数运用示例
