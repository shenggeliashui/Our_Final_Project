import os
import random
from datetime import date
import memorized
import unmemorized
import vocabulary
import pymysql
from vocabulary import change_book

# 初始化函数，用于创建已背词表和未背词表
def initialize_tables():
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象
    cursor.execute("use memorized;")  # 执行SQL语句，注意这里不返回结果，只是执行而已

    cursor.execute("DROP TABLE IF EXISTS memorized_words")
    cursor.execute('''CREATE TABLE IF NOT EXISTS memorized_words (
                    word VARCHAR(255) PRIMARY KEY,
                    memorized_date DATE)''')  # 创建已背单词表，属性为英文单词和背诵日期

    cursor.execute("DROP TABLE IF EXISTS unmemorized_words")
    cursor.execute('''CREATE TABLE IF NOT EXISTS unmemorized_words (
                      word VARCHAR(255) PRIMARY KEY)''')  # 创建未背单词表，属性为英文单词

    # 提交事务
    db.commit()

    # 关闭游标和连接
    cursor.close()
    db.close()

    print("Tables 'memorized_words' and 'unmemorized_words' initialized successfully.")

#如果未创建单词数据库，则创建（用来执行test.sql文件，避免前端直接访问数据库）
def create_database():
    # 连接到MySQL服务器
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        charset="utf8"
    )

    try:
        with connection.cursor() as cursor:
                # 查询所有数据库
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            # 检查是否存在目标数据库
            database_exists = any(db[0] == 'memorized' for db in databases)
            if database_exists is False:
                # 读取SQL文件内容
                with open("test.sql", 'r', encoding='utf-8') as file:
                    sql_commands = file.read()

                # 分割并执行SQL命令
                for command in sql_commands.split(';\n'):
                    if command.strip():
                        cursor.execute(command)
                # 提交更改
                connection.commit()
                print("SQL脚本执行成功")
    except Exception as e:
        print(f"执行SQL脚本时出错: {e}")
        connection.rollback()
    finally:
        connection.close()

#创建数据库，设置当前词库，初始化未背词库和已背词库
def main(book_id):
    create_database()
    initialize_tables()

    # 给未背词表导入所需要学习的书本单词，导入当前词典id
    change_book(book_id)


