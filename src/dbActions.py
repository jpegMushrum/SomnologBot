import pymysql
from config import host, user, password, db_name

ver = '1.1.0'

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

async def getStatistic(user_id):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT type FROM history WHERE userId = {user_id};")
    connection.commit()
    dreams = cursor.fetchall()
    data = [0, 0, 0, 0]

    for dream in dreams:
        if dream['type'] == 'usual':
            data[0] += 1
        elif dream['type'] == 'erotic':
            data[1] += 1
        elif dream['type'] == 'nightmare':
            data[2] += 1
        else:
            data[3] += 1

    connection.close()
    return data

async def addReview(text):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO reviews (version, message) VALUES ('{ver}', '{text}');")
    connection.commit()
    connection.close()

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


async def getListOfDreams(user_id, page):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT number, name FROM history WHERE userId = {user_id} AND number > {(page - 1) * 20} AND number <= {page * 20};")
    connection.commit()
    dreams = cursor.fetchall()
    connection.close()
    return dreams

async def getNumberOfDreams(user_id):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f'SELECT number FROM history WHERE userId = {user_id}')
    connection.commit()
    number = len(cursor.fetchall())
    connection.close()
    return number

async def getOneDream(user_id: int, number: int):
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT name, type, description FROM history WHERE userId = {user_id} AND number = {number};")
    connection.commit()
    dream = cursor.fetchall()
    connection.close()
    return dream[0]
