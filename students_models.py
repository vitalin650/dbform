import sqlite3


def connect_to_db(db_file='hobbies.db'):
    connect_db = sqlite3.connect(db_file)
    return connect_db


def table_creations():
    connect_db = connect_to_db()
    cursor = connect_db.cursor()
    commands = """
    CREATE TABLE IF NOT EXISTS students (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      student_full_name VARCHAR(255), latin_nickname VARCHAR(21));

    CREATE TABLE IF NOT EXISTS hobbies (
      id_hobbies INTEGER PRIMARY KEY AUTOINCREMENT,
      hobbies_name VARCHAR(35));

     CREATE TABLE IF NOT EXISTS hobby_starts (
      base_id INTEGER PRIMARY KEY AUTOINCREMENT,
      student_id INTEGER NOT NULL,
      hobby_id INTEGER NOT NULL,
      start_date VARCHAR(10),
      FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE ON UPDATE CASCADE,
      FOREIGN KEY(hobby_id) REFERENCES hobbies(id_hobbies) ON DELETE CASCADE ON UPDATE CASCADE
      );
    """
    cursor.executescript(commands)

    connect_db.commit()
    connect_db.close()


def create(tablename: str, fields: list, values: tuple):
    query_txt = F"""
    INSERT INTO {tablename} ({", ".join(fields)}) VALUES({", ".join(len(fields)*['?'])});
    """
    try:
        connect_db = connect_to_db()
        cur = connect_db.cursor()
        cur.execute(query_txt, values)
        connect_db.commit()
        print(F"""Змінні успішно вставлені в таблицю {tablename} """, end="")
        cur.close()

    except sqlite3.Error as error:
        print("Помилка SQL", error)
    finally:
        if connect_db:
            connect_db.close()
            print(".")


def read(tablename: str, fields: str, conditions: str = True, cursor=None):
    result = None
    try:
        query_txt = F"""SELECT {fields} FROM {tablename}  WHERE {conditions}"""
        result = cursor.execute(query_txt)
    except Exception as exception:
        print(f"Помилка SQL:\n==={exception}===")
    finally:
        return result


def update(tablename: str, fields: list, values: tuple):
    fileds_with_qq = [name+'=?' for name in fields[:-1]]  # last element is ID - do not take
    fields_eq_q = ", ".join(fileds_with_qq)
    record_id = fields[-1]
    query_txt = F"""
    UPDATE {tablename} SET {fields_eq_q}  WHERE {record_id}=?;
    """
    try:
        connect_db = connect_to_db()
        cur = connect_db.cursor()
        cur.execute(query_txt, values)
        connect_db.commit()
        print(F"""Дані успішно змінені в таблицї {tablename} """, end="")
        cur.close()
    except sqlite3.Error as error:
        print("Помилка SQL", error)
    finally:
        if connect_db:
            connect_db.close()
            print(".")


def delete(tablename: str, conditions: str = False):
    """DELETE from sqlitedb_developers where id = 6"""
    query_txt = F"""DELETE from {tablename} where {conditions}"""
    try:
        connect_db = connect_to_db()
        cur = connect_db.cursor()
        cur.execute(query_txt)
        connect_db.commit()
        print(F"""Видалення з {tablename} проведено """, end="")
        cur.close()

    except sqlite3.Error as error:
        print("Помилка SQLite", error)
    finally:
        if connect_db:
            connect_db.close()
            print(".")
