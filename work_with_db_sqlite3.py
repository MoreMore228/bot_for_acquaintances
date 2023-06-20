import sqlite3
import random
import config


# def tableUserCreate():
#     db = sqlite3.connect("db_id.sqlite")
#     cursor = db.cursor()
#     cursor.execute(
#         f"""CREATE TABLE {config.db_name}(
#         id INTEGER NOT NULL PRIMARY KEY,
#         user_id INTEGER,
#         user_name TEXT,
#         user_sex TEXT,
#         img_path TEXT, 
#         name TEXT,
#         user_age INTEGER,
#         user_city TEXT,
#         user_info TEXT
#         );
#         """)
#     db.close()

def random_full_user_info(self_user_id, table_name=config.table_name):
    try:
        db = sqlite3.connect(config.db_name)
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM {0} WHERE NOT user_id = {1}""".format(table_name, self_user_id))
        rows_for_return = cursor.fetchall()
        cursor.execute("""SELECT user_id FROM {0} WHERE NOT user_id = {1}""".format(table_name, self_user_id))
        rows = cursor.fetchall()
        random_int_user = random.choice([x for x in rows if x != self_user_id])
        for row in rows_for_return:
            if row[1] == random_int_user[0]:
                return row
        db.close()
    except Exception as ex:
        print(f'БД плачет: {ex}')
    finally:
        if db:
            db.close()


def insert_tuple_in_db(user_id, user_name, user_sex, img_path, name, user_age, user_city, user_info, table_name=config.table_name):
    try:
        db = sqlite3.connect(config.db_name)
        cursor = db.cursor()
        cursor.execute(
            f"""INSERT INTO {table_name}(`user_id`, `user_name`, `user_sex`, `img_path`, `name`, `user_age`, `user_city`, `user_info`) 
                       VALUES ({user_id},'{user_name}','{user_sex}','{img_path}','{name}',{user_age},'{user_city}','{user_info}')""")
        db.commit()
        db.close()
    # except
    except Exception as _ex: 
        print('Функция для работы с БД (insert_tuple_in_db) выдала ошибку: {0}'.format(_ex))
    finally:
        if db:
            db.close()


def delete_tuple_db(delete_value, delete_cur_value, table_name=config.table_name):
    try:
        # connection
        db = sqlite3.connect(config.db_name)
        cursor = db.cursor()
        # запрос на удаление
        cursor.execute("""DELETE FROM {0} WHERE {1} = {2};""".format(table_name, delete_value, delete_cur_value))
        db.commit()
        db.close()
    # exception
    except Exception as _ex:
        print('Функция для работы с БД (delete_tuple_db) выдала ошибку: {0}'.format(_ex))
    finally:
        if db:
            db.close()


def search_tuple_db(search_cur_val, table_name=config.table_name, search_val='user_id'):
    try:
        # connection
        db = sqlite3.connect(config.db_name)
        cursor = db.cursor()
        # запрос на удаление
        cursor.execute("""SELECT * FROM {0} WHERE {1} = {2}""".format(table_name, search_val, search_cur_val))
        row = cursor.fetchone()
        return row
    # exception      
    except Exception as _ex:
        print('Функция для работы с БД (search_tuple_db) выдала ошибку: {0}'.format(_ex))
    finally:
        if db:
            db.close()


def check_table(table_name=config.table_name):
# connection
    try:
        db = sqlite3.connect(config.db_name)
        cursor = db.cursor()

        
        cursor.execute(
            """SELECT * FROM {0}""".format(table_name)
        )
        rows = cursor.fetchall()
        print('#' * 20)
        for row in rows:
            print(row)
        print('#' * 20)
    except Exception as _ex:
        print('Функция для работы с БД (check_table) выдала ошибку{0}'.format(_ex))
    finally:
        if db:
            db.close()