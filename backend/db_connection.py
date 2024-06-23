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
            database='words_db',
            user='root',
            password='123456'
        )
        if connection.is_connected():
            print("已连接到 MySQL 数据库")
            return connection
    except Error as e:
        print("连接 MySQL 时出错: {}".format(e))
    return None

