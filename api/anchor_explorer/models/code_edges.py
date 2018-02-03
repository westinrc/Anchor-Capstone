import pymysql

class Code_Edges(object):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    current_index = 1

    def __init__(self, code, edge):
        self.index = Code_Edges.current_index
        self.code = code
        self.edge = edge

    def store(self):
        sql = sql = "INSERT INTO code_edges (`index`, code, edge) VALUES (%s, %s, %s)"
        Code_Edges.cursor.execute(sql, (self.index, self.code, self.edge))
        Code_Edges.conn.commit()
        Code_Edges.current_index = Code_Edges.current_index + 1

    def get_data(self, index):
        sql = "SELECT * FROM code_edges WHERE `index` = %s"
        Code_Edges.cursor.execute(sql, index)
        result = Code_Edges.cursor.fetchone()
        self.code = result['code']
        self.edge = result['edge']

    @staticmethod
    def get_count():
        sql = "SELECT COUNT(*) FROM code_edges"
        Code_Edges.cursor.execute(sql)
        result = Code_Edges.cursor.fetchone()
        count = result['COUNT(*)']
        return count
