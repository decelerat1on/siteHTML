import sqlite3
# Создание таблицы
#    CREATE TABLE users(
#    id integer primary key,
#   login nvarchar(50),
#  password nvarchar(50))
def connection(sql):
    with sqlite3.connect('test.db') as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
def add_user(data):
    query = f'''
    INSERT INTO users('login','password')
    VALUES ('{data['login']}','{data['password']}')
    
    '''
    connection(query)

def check_user(data):
    query = f'''
    SELECT login, password
    FROM users    
    '''
    res = connection(query)
    for user in res:
        if data['login'] == user[0]:
            if data['password'] == user[1]:
                return 'Вы вошли в свой аккаунт'
        else:
            return 'Пользователя с таким логин/пароль не существуем'




