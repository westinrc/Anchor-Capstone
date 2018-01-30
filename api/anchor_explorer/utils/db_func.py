import pymysql
import os
import sys
import subprocess
import string
sys.path.append("..")
from models.visit import Visit
from models.secondary_icd9 import Secondary_ICD_9
from models.code_names import Code_Names
from models.code_edges import Code_Edges

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Capstone_Password', db='capstone_DB')
cursor = conn.cursor()

def upload_pitt_data(pitt_file):
    

    if pitt_file is not None:
        for line in pitt_file:
            split_parts = line.split("|")

            current_index = int(split_parts[0])
            primary_icd_9 = split_parts[4]
            note_type = split_parts[2]
            chief_complaint = split_parts[3]
            note_text = split_parts[7]
            date = split_parts[6]

            new_visit = Visit(current_index, primary_icd_9, note_type, chief_complaint, note_text, date)
            new_visit.store()
        
            icd_9_codes = split_parts[5]
            icd_9_split = icd_9_codes.split(",")
            for code in icd_9_split:
                if code != '':
                    new_secondary_icd_9_entry = Secondary_ICD_9(current_index, code)
                    new_secondary_icd_9_entry.store()

            current_index = current_index + 1
        return "Success!"
    else:
        return "File Upload Error"


printable = set(string.printable)
def sanitize(txt):
    txt = ''.join(filter(lambda c: c in printable, txt)) 
    return txt

def traverse(t):
    new_code_names_entry = Code_Names(t.code, t.description)
    new_code_names_entry.store()
    for c in t.children:
        traverse(c)

def getEdges(t):
    for c in t.children:
        new_code_edges_entry = Code_Edges(t.code, c.code)
        new_code_edges_entry.store()
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