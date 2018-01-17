import pymysql
import os

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')

def upload_pitt_data():
    file_path = os.path.join(os.path.dirname(__file__), "pitt-delimited.txt")
    pitt_file = open(file_path, "r")
    for line in pitt_file:
        split_parts = line.split("|")
        result = split_parts[3]
        #TODO: figure out which information is which and where it should go, then store
        # in the table
        break
    return result
    # cursor = conn.cursor()
    # sql = "INSERT INTO visit (`index`, MDComments, Age, Sex, ChiefComplainr, TriageAssessment) VALUES (1, 'Idk', 22, 'M', 'not working', 'work')"
    # cursor.execute(sql)
    # sql = "INSERT INTO patient (`index`, firstName, lastName, DOB) VALUES (1, 'Test', 'Person', '1997-11-19 00:00:00')"
    # cursor.execute(sql)
    # conn.commit()

#Used for development
def clear_tables():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM visit;")
    cursor.execute("DELETE FROM patient")
    conn.commit()