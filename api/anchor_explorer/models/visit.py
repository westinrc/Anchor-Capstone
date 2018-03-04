import pymysql

class Visit(object):
    conn = pymysql.connect(host='127.0.0.1', user='capstone', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    def __init__(self, index=None, primary_ICD_9=None, note_type=None, chief_complaint=None, note_text=None, date=None):
        self.index = index
        self.primary_ICD_9 = primary_ICD_9
        self.note_type = note_type
        self.chief_complaint = chief_complaint
        self.note_text = note_text
        self.date = date

    def store(self):
        sql = "INSERT INTO visit (`index`, primary_ICD_9, note_type, chief_complaint, note_text, date) VALUES (%s, %s, %s, %s, %s, %s)"
        Visit.cursor.execute(sql, (self.index, self.primary_ICD_9, self.note_type, self.chief_complaint, self.note_text, self.date))
        Visit.conn.commit()

    @staticmethod
    def get_count():
        sql = "SELECT COUNT(*) FROM visit"
        Visit.cursor.execute(sql)
        result = Visit.cursor.fetchone()
        count = result['COUNT(*)']
        return count

    @staticmethod
    def retrieve_all_visits():
        sql = "SELECT * FROM visit"
        Visit.cursor.execute(sql)
        result = Visit.cursor.fetchall()
        return result
