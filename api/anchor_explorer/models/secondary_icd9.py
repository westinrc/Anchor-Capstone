import pymysql

class Secondary_ICD_9(object):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    def __init__(self, index=None, code=None):
        self.index = index
        self.code = code
    
    def store(self):
        sql = "INSERT INTO ICD_9 (`index`, code) VALUES (%s, %s)"
        Secondary_ICD_9.cursor.execute(sql, (self.index, self.code))
        Secondary_ICD_9.conn.commit()

    @staticmethod
    def retrieve_by_index(index):
        sql = "SELECT * FROM ICD_9 WHERE `index` = " + index
        Secondary_ICD_9.cursor.execute(sql)
        result = Secondary_ICD_9.cursor.fetchall()
        return result