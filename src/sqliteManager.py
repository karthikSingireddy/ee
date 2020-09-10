import sqlite3

# conn = sqlite3.connect('data.db')

# cursor = conn.cursor()

# params = ['test', 'original']

# cursor.execute('''
#             INSERT INTO images
#             (image, blur_type)
#             VALUES(?,?)

# ''', params)

# data = cursor.fetchone()

# print(data)


# conn.commit()
# conn.close()

# print('done')


def initConnection():
    conn = sqlite3.connect('data.db')
    return conn

def closeConnection(conn):
    conn.close()

def insertImage(conn, image: str, blur_type: str, image_index: int):
    cursor = conn.cursor()
    
    sql: str = '''
                INSERT INTO images
                (image, blur_type, image_index)
                VALUES(?,?,?)
    '''
    params = [image, blur_type, image_index]

    cursor.execute(sql, params)

    conn.commit()

def getImage(conn, blur_type, image_index):
    cursor = conn.cursor()

    sql: str = '''
                SELECT image FROM images
                WHERE blur_type = ? AND image_index = ?;
    '''

    params = [blur_type, image_index]

    cursor.execute(sql, params)
    val = cursor.fetchone()

    conn.commit()

    return val
