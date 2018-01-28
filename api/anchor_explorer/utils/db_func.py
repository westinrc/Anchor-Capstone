import pymysql
import os
import sys
import subprocess
import string

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')
cursor = conn.cursor()

def upload_pitt_data(pitt_file):
    

    if pitt_file is not None:
        for line in pitt_file:
            split_parts = line.split("|")
            current_index = int(split_parts[0])

            visit_sql = "INSERT INTO visit (`index`, primary_ICD_9, note_type, chief_complaint, note_text, date) VALUES (%s, %s, %s, %s, %s, %s)"
            primary_icd_9 = split_parts[4]
            note_type = split_parts[2]
            chief_complaint = split_parts[3]
            note_text = split_parts[7]
            date = split_parts[6]
            cursor.execute(visit_sql, (current_index, primary_icd_9, note_type, chief_complaint, note_text, date))
        
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


printable = set(string.printable)
def sanitize(txt):
    txt = ''.join(filter(lambda c: c in printable, txt)) 
    return txt

def traverse(t):
    #print>>outfile, sanitize(t.code+'\t'+t.description)
    sql = "INSERT INTO code_names (code, name) VALUES (%s, %s)"
    cursor.execute(sql, (t.code, t.description))
    conn.commit()
    for c in t.children:
        traverse(c)

def getEdges(t):
    for c in t.children:
        #print >>outfile, sanitize(t.code+'\t'+c.code)
        sql = "INSERT INTO code_edges (code, edge) VALUES (%s, %s)"
        cursor.execute(sql, (t.code, c.code))
        conn.commit()
        getEdges(c)

def load_icd9_structure():
    print 'cloning github repository sirrice/icd9.git'
    subprocess.call('git clone https://github.com/sirrice/icd9.git', shell=1)

    sys.path.append('icd9')
    from icd9 import ICD9

    tree = ICD9('icd9/codes.json')
    toplevelnodes = tree.children

    traverse(tree)

    getEdges(tree)

#Used for development
def clear_tables():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM visit;")
    cursor.execute("DELETE FROM patient;")
    cursor.execute("DELETE FROM ICD_9;")
    cursor.execute("DELETE FROM code_names;")
    cursor.execute("DELETE FROM code_edges;")
    conn.commit()