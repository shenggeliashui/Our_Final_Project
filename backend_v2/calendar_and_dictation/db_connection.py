# -*- coding: utf-8 -*-
# db_connection.py
"""
此模块提供与 MySQL 数据库的连接功能。
"""

import mysql.connector
from mysql.connector import Error

def get_connection():
    """
    连接到 MySQL 数据库。
    
    返回:
        connection: MySQL 数据库连接对象。
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='memorized',
            user='root',
            password='123456'
        )
        if connection.is_connected():
            print("已连接到 MySQL 数据库")
            return connection
    except Error as e:
        print("连接 MySQL 时出错: {}".format(e))
    return None
    
    
def get_user_connection():
    """
    连接到 MySQL 数据库。
    
    返回:
        connection: MySQL 数据库连接对象。
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='wordapp',
            user='root',
            password='123456'
        )
        if connection.is_connected():
            print("已连接到 MySQL 数据库")
            return connection
    except Error as e:
        print("连接 MySQL 时出错: {}".format(e))
    return None
    
def get_book_id():
    """
    连接数据库，获取 user 表中的 cur_book 字段，返回书籍 ID 字符串。
    
    返回:
        book_id (str): 当前书籍的 ID。
    """
    connection = get_user_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT cur_book FROM user")
        result = cursor.fetchone()
        if result:
            book_id = result[0]
            return str(book_id)
        else:
            print("user 表中没有 cur_book 字段的记录")
            return None
    except Error as e:
        print("查询数据库时出错: {}".format(e))
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL 连接已关闭")



