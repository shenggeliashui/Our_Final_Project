import random
import pymysql


# 获取未背单词表中单词数量
def get_unmemorized_num():
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    cursor.execute("SELECT COUNT(*) FROM unmemorized_words")
    count = cursor.fetchone()[0]  # 获取查询结果的第一行第一列

    # 关闭游标和连接
    cursor.close()
    db.close()

    return count


# 从未背词库中随机抽取并返回单词
def random_get_word_unmemorized():
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    # 查询未背词库中的单词数量
    cursor.execute("SELECT COUNT(*) FROM unmemorized_words")
    count = cursor.fetchone()[0]

    # 如果未背词库为空，返回空字符串
    if count == 0:
        print("Your unmemorized_vocabulary is empty, please add new words.")
        return ""

    # 随机选择一个单词
    offset = random.randint(0, count - 1)
    select_word = "SELECT word FROM unmemorized_words LIMIT 1 OFFSET %s"
    cursor.execute(select_word, (offset,))
    word = cursor.fetchone()[0]

    # 关闭游标和连接
    cursor.close()
    db.close()

    return word


# 删除未背词库中的指定单词
def delete_unmemorized_word(word):
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    # 删除指定单词
    delete_word = "DELETE FROM unmemorized_words WHERE word = %s"
    cursor.execute(delete_word, (word,))

    # 提交更改
    db.commit()

    # 检查是否删除成功
    if cursor.rowcount > 0:
        print(f"Word '{word}' deleted from unmemorized vocabulary.")
    else:
        print(f"Word '{word}' not found in unmemorized vocabulary. No deletion.")

    # 关闭游标和连接
    cursor.close()
    db.close()


# 给未背词表导入所需要学习的书本单词
def transfer_to_unmemorized(book_id):
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    if book_id != 'CET4':
        book_id = book_id + '_2'
    # 查询符合条件的数据，并将 word 插入到 unmemorized 表中
    query = "INSERT IGNORE INTO unmemorized_words (word) SELECT word FROM words WHERE bookId = %s"
    cursor.execute(query, (book_id,))

    # 提交事务
    db.commit()

    # 关闭游标和连接
    cursor.close()
    db.close()

    print(f"Words from bookId {book_id} transferred to 'unmemorized' table successfully.")


# 清空未背词表
def clear_unmemorized_vocabulary():
    # 连接到数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="memorized", charset="utf8")
    cursor = db.cursor()  # 创建一个游标对象

    # 执行清空表的操作
    query = "TRUNCATE TABLE unmemorized_words"
    cursor.execute(query)

    # 提交事务
    db.commit()

    # 关闭游标和连接
    cursor.close()
    db.close()

    print("Table 'unmemorized_words' has been cleared successfully.")
