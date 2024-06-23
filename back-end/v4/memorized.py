import os
import random
from datetime import date
import pymysql


# 获取已背单词表中单词数量
def get_memorized_num():
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    cursor.execute("SELECT COUNT(*) FROM memorized_words")
    count = cursor.fetchone()[0]  # 获取查询结果的第一行第一列

    # 关闭游标和连接
    cursor.close()
    db.close()

    return count


# 增加单词到已背单词表中
def add_memorized_word(word, date):
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()

    # 插入新单词和日期
    add_word = "INSERT IGNORE INTO memorized_words (word, memorized_date) VALUES (%s, %s)"
    data_word = (word, date)
    cursor.execute(add_word, data_word)

    db.commit()  # 提交更改

    # 检查是否插入成功
    if cursor.rowcount == 1:
        print(f"Word '{word}' added to the vocabulary.")
    else:
        print(f"Word '{word}' already exists in the vocabulary. Did not add.")

    cursor.close()
    db.close()


# 清空已背词表
def clear_memorized_vocabulary():
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    # 执行清空表的操作
    query = "TRUNCATE TABLE memorized_words"
    cursor.execute(query)

    # 提交事务
    db.commit()

    # 关闭游标和连接
    cursor.close()
    db.close()

    print("Table 'memorized_words' has been cleared successfully.")
