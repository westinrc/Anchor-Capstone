import pymysql

class Word_indexes(object):
    conn = pymysql.connect(host='127.0.0.1', user='capstone', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    def __init__(self, word, index):
        self.word = word
        self.index = index
    
    def store(self):
        sql = "INSERT into word_indexes (word, `index`) VALUES (%s, %s)"
        Word_indexes.cursor.execute(sql, (self.word, self.index))
        Word_indexes.conn.commit()