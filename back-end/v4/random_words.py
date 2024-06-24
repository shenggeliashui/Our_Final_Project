# random_words.py
from db_connection import get_connection
from mysql.connector import Error

def get_random_words_info(book_id):
    connection = get_connection()
    try:
        if connection:
            cursor = connection.cursor()
            query = """
            SELECT word
            FROM test_table
            WHERE bookId = %s
            ORDER BY RAND()
            LIMIT 10
            """
            cursor.execute(query, (book_id,))
            random_words = cursor.fetchall()

            # 创建或清空临时表
            cursor.execute("CREATE TEMPORARY TABLE IF NOT EXISTS temp_words (word VARCHAR(255), bookId VARCHAR(255), cursor INT AUTO_INCREMENT PRIMARY KEY)")
            cursor.execute("TRUNCATE TABLE temp_words")
            
            # 插入随机抽取的单词到临时表
            for word in random_words:
                query = """
                INSERT INTO temp_words (word, bookId)
                VALUES (%s, %s)
                """
                cursor.execute(query, (word[0], book_id))
            
            # 创建游标并指向第一行
            cursor.execute("SELECT word, bookId FROM temp_words LIMIT 1")
            cursor.fetchone()  # 将游标指向第一行

            connection.commit()
            return True
    except Error as e:
        print("连接 MySQL 时出错: {}".格式(e))
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def get_current_word():
    connection = get_connection()
    try:
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT word, bookId FROM temp_words LIMIT 1")
            current_word = cursor.fetchone()
            return current_word
    except Error as e:
        print("连接 MySQL 时出错: {}".格式(e))
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def update_cursor():
    connection = get_connection()
    try:
        if connection:
            cursor = connection.cursor()
            # 获取当前游标位置
            cursor.execute("SELECT MIN(cursor) FROM temp_words WHERE cursor > (SELECT MIN(cursor) FROM temp_words)")
            next_cursor = cursor.fetchone()
            if next_cursor and next_cursor[0] is not None:
                # 删除当前最小游标行，模拟游标前进
                cursor.execute("DELETE FROM temp_words WHERE cursor = (SELECT MIN(cursor) FROM temp_words)")
                connection.commit()
                return next_cursor
            else:
                # 如果没有更多行，清空表
                cursor.execute("TRUNCATE TABLE temp_words")
                connection.commit()
                return None
    except Error as e:
        print("连接 MySQL 时出错: {}".格式(e))
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

