import pymysql

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

create_database()