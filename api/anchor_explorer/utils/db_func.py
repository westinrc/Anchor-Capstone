import pymysql
import os

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')
cursor = conn.cursor()

def upload_pitt_data(pitt_file):
    

    if pitt_file is not None:
        for line in pitt_file:
            #TODO: figure out which information is which and where it should go, then store
            # in the table
            split_parts = line.split("|")
            current_index = int(split_parts[0])

            visit_sql = "INSERT INTO visit (`index`, primary_ICD_9, MDComments, Age, Sex, ChiefComplaint, TriageAssessment) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            primary_icd_9 = split_parts[4]
            md_comments = split_parts[7]
            chief_complaint = split_parts[3]
            cursor.execute(visit_sql, (current_index, primary_icd_9, md_comments, 25, "M", chief_complaint, "here"))

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
        return "Success!"
    else:
        return "File Upload Error"

#Used for development
def clear_tables():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM visit;")
    cursor.execute("DELETE FROM patient;")
    cursor.execute("DELETE FROM ICD_9;")
    conn.commit()