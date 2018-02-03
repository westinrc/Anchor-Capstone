import pymysql

class Code_Names(object):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    current_index = 1

    def __init__(self, code, name):
        self.index = Code_Names.current_index
        self.code = code
        self.name = name

    def store(self):
        sql = "INSERT INTO code_names (`index`, code, name) VALUES (%s, %s, %s)"
        Code_Names.cursor.execute(sql, (self.index, self.code, self.name))
        Code_Names.conn.commit()
        Code_Names.current_index = Code_Names.current_index + 1

    def get_data(self, index):
        sql = "SELECT * FROM code_names WHERE `index` = %s"
        Code_Names.cursor.execute(sql, index)
        result = Code_Names.cursor.fetchone()
        self.code = result['code']
        self.name = result['name']

    @staticmethod
    def get_count():
        sql = "SELECT COUNT(*) FROM code_names"
        Code_Names.cursor.execute(sql)
        result = Code_Names.cursor.fetchone()
        count = result['COUNT(*)']
        return count
