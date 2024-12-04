import sqlite3

DB_FILE = "kow.db"

CREATE_SQL_FILE = "resource/create.sql"


def create_connection(db_file) -> sqlite3.Connection:
    print("Connecting to database...")
    conn = sqlite3.connect(db_file)
    return sqlite3.connect(db_file)


def create_kow_table(connection: sqlite3.Connection):
    sql_file = open(CREATE_SQL_FILE, 'r', encoding='utf-8')
    sql_file_content = sql_file.read()
    print("Execute SQL: \n{}".format(sql_file_content))
    sql_file.close()
    connection.cursor().execute(sql_file_content)


def init_db():
    print("Initializing database...")
    conn = sqlite3.connect(DB_FILE)
    connection = create_connection(DB_FILE)
    create_kow_table(connection)
    print("Database initialized.")


if __name__ == '__main__':
    init_db()
