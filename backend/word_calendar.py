import calendar
from db_connection import get_connection
from mysql.connector import Error

def get_word_count_and_levels(year, month):
    connection = None
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            days_in_month = calendar.monthrange(year, month)[1]
            result = []

            query = """
            SELECT DAY(random_date) as day, COUNT(*) as count
            FROM test_table
            WHERE YEAR(random_date) = %s AND MONTH(random_date) = %s
            GROUP BY DAY(random_date)
            """
            cursor.execute(query, (year, month))
            rows = cursor.fetchall()

            word_data = {row[0]: row[1] for row in rows}

            for day in range(1, 32):  # 遍历1到31号的每一天
                if day <= days_in_month:
                    count = word_data.get(day, 0)
                    level = 1

                    if count > 60:
                        level = 5
                    elif count > 30:
                        level = 4
                    elif count > 10:
                        level = 3
                    elif count > 0:
                        level = 2

                    result.append({'date': day, 'words': count, 'level': level, 'checked': True})
                else:
                    result.append({'date': day, 'words': -1, 'level': -1, 'checked': False})

            return result

    except Error as e:
        print("连接 MySQL 时出错: {}".format(e))
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
