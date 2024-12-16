import os
import sqlite3

from app import STATIC_SQL_DIR, DATA_DIR

SQLITE_DB_FILE = os.path.join(DATA_DIR, "kow.db")
CREATE_SQL_FILE = os.path.join(STATIC_SQL_DIR, "create.sql")


# 创建数据库连接
def create_connection(db_file) -> sqlite3.Connection:
    print("Connecting to database...")
    return sqlite3.connect(db_file)


# 创建基础表
def create_kow_table(connection: sqlite3.Connection):
    try:
        with open(CREATE_SQL_FILE, 'r', encoding='utf-8') as sql_file:
            sql_file_content = sql_file.read()
            print("Execute SQL: \n{}".format(sql_file_content))
            connection.executescript(sql_file_content)
            connection.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


# 初始化数据库
def init_db():
    print("Initializing database...")
    with create_connection(SQLITE_DB_FILE) as connection:
        create_kow_table(connection)
    print("Database initialized.")


# 保存按钮点击事件
def save_key_event(key: str):
    print("Save key event...")
    with create_connection(SQLITE_DB_FILE) as connection:
        connection.cursor().execute("INSERT INTO key_events(key) VALUES (?)", (key.lower(),))
        connection.commit()


# 查询指定时间的键盘点击事件
def get_key_event(key: str):
    con = create_connection(SQLITE_DB_FILE)
    con.execute("SELECT * FROM key_events WHERE key = ?", (key,))
    return key


if __name__ == '__main__':
    init_db()
