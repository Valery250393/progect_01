
# Самостоятельная работа №1

# 1. Создание таблицы Students

# import sqlite3

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = '''
# CREATE TABLE Students (
# Student_ID INTEGER NOT NULL,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY
# );
# '''
# cursor.execute(query)
# connection.commit()
# connection.close()

# 2. Заполнение таблицы Students

# import sqlite3

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = '''
# INSERT INTO Students (Student_ID, Student_Name, School_Id)
# VALUES
# ('201', 'Иван', 1),
# ('202', 'Петр', 2),
# ('203', 'Анастасия', 3),
# ('204', 'Игорь', 4);
# '''
# cursor.execute(query)
# connection.commit()
# connection.close()

#  Написать программу, с помощью которой по ID студента можно получать информацию
# о школе и студенте.

# Формат вывода:
# • ID студента:
# • Имя студента:
# • ID школы:
# • Название школы:

import sqlite3

def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_school_name(school_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = '''SELECT * FROM School WHERE School_ID = ?'''
        cursor.execute(select_query, (school_id,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1]
    except (Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных', error)

def get_students(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = '''SELECT * FROM Students WHERE Student_ID = ?'''
        cursor.execute(sql_select_query, (student_id,))
        records = cursor.fetchall()
        print('\nДанные по студенту')
        for row in records:
            print('ID Студента:', row[0])
            print('Имя Студента:', row[1])
            print('ID Школы:', row[2])
            print('Название Школы:', get_school_name(row[2]), '\n')
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
         print('Ошибка в получении данных', error)

print('\nДомашняя работа. Вывести данные о школе и студенте по ID студента')
get_students(204)

# Выполнено
