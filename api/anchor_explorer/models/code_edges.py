import pymysql

class Code_Edges(object):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor()

    def __init__(self, code, edge):
        self.code = code
        self.edge = edge

    def store(self):
        sql = sql = "INSERT INTO code_edges (code, edge) VALUES (%s, %s)"
        Code_Edges.cursor.execute(sql, (self.code, self.edge))
        Code_Edges.conn.commit()