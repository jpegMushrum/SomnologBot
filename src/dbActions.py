import pymysql
from config import host, user, password, db_name

async def addUser(user_id, user_name):
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

async def changeUserName(user_id, user_name):
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

async def checkUser(user_id):
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

async def getName(user_id):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT userName FROM clients WHERE id = {user_id};")
    connection.commit()
    name = cursor.fetchall()
    connection.close()
    return name[0]['userName']

async def addDream(user_id, name, dream_type, description):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM history WHERE userId = {user_id};")
    connection.commit()
    number = len(cursor.fetchall()) + 1
    cursor.execute(f"INSERT INTO `history` (userId, number, name, type, description) VALUES ({user_id}, {number}, \'{name}\', \'{dream_type}\', \'{description}\');")
    connection.commit()
    connection.close()

async def deleteLastDream(user_id):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM history WHERE userId = {user_id};")
    connection.commit()
    number = len(cursor.fetchall())
    cursor.execute(f"DELETE FROM history WHERE userId = {user_id} AND number = {number};")
    connection.commit()
    connection.close()


async def clearDreamHistory(user_id):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM history WHERE userId = {user_id};")
    connection.commit()
    connection.close()

