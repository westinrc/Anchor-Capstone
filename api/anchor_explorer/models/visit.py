import pymysql

class Visit(object):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')
    cursor = conn.cursor()

    def __init__(self, index, primary_ICD_9, note_type, chief_complaint, note_text, date):
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