import os
import random
from datetime import date
import pymysql
from unmemorized import clear_unmemorized_vocabulary,transfer_to_unmemorized
from memorized import clear_memorized_vocabulary
# 定义当前词典id
book_id = "SAT"

# 定义函数，修改词典
def change_book(new_book_id):
    global book_id  # 声明要使用的全局变量
    book_id = new_book_id   # 修改全局变量的值
    #修改词典id后，清空原未背词库和已被词库
    clear_memorized_vocabulary()
    clear_unmemorized_vocabulary()

    #重新导入未背词库表
    transfer_to_unmemorized(book_id)

    
# 根据单词从完整词库中获取并返回音标
def get_word_phonetic(word):
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    # 查询单词的美式和英式发音
    query = "SELECT usphone, ukphone FROM words WHERE word = %s"
    cursor.execute(query, (word,))

    # 提取查询结果
    result = cursor.fetchone()

    # 关闭游标和连接
    cursor.close()
    db.close()

    if result:
        usphone = result[0]
        ukphone = result[1]
        return usphone, ukphone
    else:
        print(f"Word '{word}' not found in the database.")
        return None, None


# 根据单词从完整词库中获取并返回字典
def get_word_meaning(word):
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    # 查询单词的词性、词义和书籍ID
    if book_id != 'CET4':
        use_book_id = book_id + '_2'
    query = "SELECT pos, tranCn FROM words WHERE word = %s AND bookId = %s"
    cursor.execute(query, (word, use_book_id))

    # 初始化一个空字典，用于存储词性和对应的词义列表
    word_dict = {}

    # 处理查询结果
    for (pos, tranCn) in cursor:
        # part 是词性，meaning 是对应的词义
        if pos in word_dict:
            word_dict[pos].append(tranCn)
        else:
            word_dict[pos] = [tranCn]

    # 关闭游标和连接
    cursor.close()
    db.close()

    return word_dict


# 根据单词从完整词库中获取例句字典{英文例句,中文翻译}
def get_word_example(word):
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    # 查询单词的例句和中文翻译
    if book_id != 'CET4':
        use_book_id = book_id + '_2'
    query = "SELECT sContent, sCn FROM words WHERE word = %s AND bookId = %s"
    cursor.execute(query, (word, use_book_id))

    # 初始化一个空字典，用于存储例句和翻译
    example_dict = {}

    # 处理查询结果
    for (sContent, sCn) in cursor:
        # sContent 是例句（英文），sCn 是中文翻译
        example_dict[sContent] = sCn

    # 关闭游标和连接
    cursor.close()
    db.close()

    return example_dict

# 清空整个数据库
def clear_Memorized_Database():
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    # 执行清空表的操作
    query = "DROP DATABASE memorized"
    cursor.execute(query)

    # 提交事务
    db.commit()

    # 关闭游标和连接
    cursor.close()
    db.close()

    print("DATABASE memorized has been cleared successfully.")