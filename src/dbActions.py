import pymysql
from config import host, user, password, db_name

def addUser(user_id, user_name):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO `clients` (id, userName) VALUES ({user_id}, \'{user_name}\');")
    connection.commit()
    connection.close()

def changeUserName(user_id, user_name):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM clients WHERE id = {user_id};")
    connection.commit()
    cursor.execute(f"INSERT INTO `clients` (id, userName) VALUES ({user_id}, \'{user_name}\');")
    connection.commit()
    connection.close()

def checkUser(user_id):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM clients WHERE id = {user_id};")
    connection.commit()
    res = cursor.fetchall()
    connection.close()
    if len(res) == 0:
        return False
    else:
        return True

def getName(user_id):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT userName FROM clients WHERE id = {user_id}")
    connection.commit()
    name = cursor.fetchall()
    connection.close()
    return name[0]['userName']