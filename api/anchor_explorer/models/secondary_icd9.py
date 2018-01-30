import pymysql

class Secondary_ICD_9(object):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor()

    def __init__(self, index, code):
        self.index = index
        self.code = code
    
    def store(self):
        sql = "INSERT INTO ICD_9 (`index`, code) VALUES (%s, %s)"
        Secondary_ICD_9.cursor.execute(sql, (self.index, self.code))
        Secondary_ICD_9.conn.commit()