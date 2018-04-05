import pymysql

class Secondary_ICD_9(object):
    conn = pymysql.connect(host='127.0.0.1', user='capstone', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    def __init__(self, index=None, code=None):
        self.index = index
        self.code = code
    
    def store(self):
        sql = "INSERT INTO ICD_9 (`index`, code) VALUES (%s, %s)"
        Secondary_ICD_9.cursor.execute(sql, (self.index, self.code))
        Secondary_ICD_9.conn.commit()

    @staticmethod
    def retrieve_all_ICD_9():
        sql = "SELECT `index`, GROUP_CONCAT(code SEPARATOR ', ') AS codes FROM ICD_9 GROUP BY `index`;"
        Secondary_ICD_9.cursor.execute(sql)
        result = Secondary_ICD_9.cursor.fetchall()
        return result