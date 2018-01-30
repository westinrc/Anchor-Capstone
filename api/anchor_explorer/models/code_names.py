import pymysql

class Code_Names(object):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor()

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def store(self):
        sql = "INSERT INTO code_names (code, name) VALUES (%s, %s)"
        Code_Names.cursor.execute(sql, (self.code, self.name))
        Code_Names.conn.commit()