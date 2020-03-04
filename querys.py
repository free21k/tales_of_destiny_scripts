'''
Test for sqlite3
'''
import sqlite3
DB_FILE = 'scripts.db'
def find_charactor_id(name):
    '''
    find charactor id from charactors table.
    :parameter {name} : to find.
    :return {charactor_id} : charactors index
    '''
    if name is None or name == "":
        return -1

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    query = """SELECT idx, name, image
    FROM `charactors` WHERE name like '%{0}%';""".format(name)

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return 0

    return rows[0][0]

def insert_script(chaptor_id, charactor_id, charactor_name, message):
    '''
    insert message into messages table.
    :parameter {chaptor_id} : chaptor index.
    :parameter {charactor_id} : charactor index.
    :parameter {message} : message.
    :return {} : None
    '''
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    query = """INSERT INTO `messages` (chapter_id, charactor_id, charactor_name, message)
    VALUES ({0}, {1}, '{2}', '{3}')""".format(chaptor_id, charactor_id, charactor_name, message)

    cursor.execute(query)
    conn.commit()
    conn.close()

def insert_script_with_charactor_name(chaptor_id, charactor_name, message):
    '''
    insert message into messages table by charactor_name.
    :parameter {chaptor_id} : chaptor index.
    :parameter {charactor_id} : charactor index.
    :parameter {message} : message.
    :return {} : None
    '''
    if charactor_name is None:
        charactor_name = ""
    charactor_id = find_charactor_id(charactor_name)
    insert_script(chaptor_id, charactor_id, charactor_name, message)
