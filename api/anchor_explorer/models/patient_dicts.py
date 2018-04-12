import pymysql

class Patient_dicts(object):
    conn = pymysql.connect(host='127.0.0.1', user='capstone', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    def __init__(self, index=None, dictionary=None):
        self.index = index
        self.dictionary=dictionary

    def store(self):
        sql = "INSERT INTO patient_dicts (`index`, dict) VALUES (%s, %s)"
        Patient_dicts.cursor.execute(sql, (self.index, self.dictionary))
        Patient_dicts.conn.commit()