import pymysql
import os

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')

def upload_pitt_data():
    #TODO: Set up API to have pitt-data file sent over the network instead of opened locally
    cursor = conn.cursor()
    file_path = os.path.join(os.path.dirname(__file__), "pitt-delimited.txt")
    pitt_file = open(file_path, "r")

    current_index = 0
    for line in pitt_file:
        #TODO: figure out which information is which and where it should go, then store
        # in the table
        split_parts = line.split("|")

        visit_sql = "INSERT INTO visit (`index`, MDComments, Age, Sex, ChiefComplaint, TriageAssessment) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(visit_sql, (current_index, "Not sure", 25, "M", "what will go", "here"))

        patient_sql = "INSERT INTO patient (`index`, firstName, lastName, DOB) VALUES (%s, %s, %s, %s)"
        cursor.execute(patient_sql, (current_index, "Just want", "to get something done", "1995-11-16 00:00:00"))
        
        icd_9_codes = split_parts[5]
        icd_9_split = icd_9_codes.split(",")
        for code in icd_9_split:
            if code != '':
                icd_9_sql = "INSERT INTO ICD_9 (`index`, code) VALUES (%s, %s)"
                cursor.execute(icd_9_sql, (current_index, code))
        conn.commit()
        current_index = current_index + 1
        

#Used for development
def clear_tables():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM visit;")
    cursor.execute("DELETE FROM patient;")
    cursor.execute("DELETE FROM ICD_9;")
    conn.commit()