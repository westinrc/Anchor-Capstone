import pymysql
import os
import sys
import subprocess
import string
import networkx as nx
import cPickle as pickle
import re
from Structures import Structure
sys.path.append("..")
from models.visit import Visit
from models.secondary_icd9 import Secondary_ICD_9
from models.code_names import Code_Names
from models.code_edges import Code_Edges

conn = pymysql.connect(host='127.0.0.1', user='capstone', passwd='Capstone_Password', db='capstone_DB')
cursor = conn.cursor()

def upload_pitt_data(pitt_file):
    if pitt_file is not None:
        current_index = 0
        for line in pitt_file:
            split_parts = line.split("|")

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
    current_names_index = 1
    current_edges_index = 1

    traverse(tree)

    getEdges(tree)


def build_structured_rep(data_type):
    # try:
    #     datatype = sys.argv[1]
    #     names = sys.argv[2]+'.names'
    #     edges = sys.argv[2]+'.edges'
    # except:
    #     print "usage: python build_structured_rep.py type src"
    #     sys.exit()
    

    try:
        os.makedirs('Structures')
    except:
        pass

    print 'building a structured representation of', data_type
    print 'assuming prefix', data_type+'_'
    prefix = data_type+'_'

    
    nameDict = {}
    name_count = Code_Names.get_count()
    name_obj = Code_Names(None, None)
    for i in range(1, name_count + 1):
        name_obj.get_data(i)
        code = name_obj.code
        name = name_obj.name
        code = prefix+code
        nameDict[code] = name

    #f = file(edges)
    graph = nx.DiGraph()

    for code,name in nameDict.items():
        graph.add_node(code, name=name)

    edge_count = Code_Edges.get_count()
    edge_obj = Code_Edges(None, None)
    for i in range(1, edge_count + 1):
        edge_obj.get_data(i)
        parent = edge_obj.code
        child = edge_obj.edge
        graph.add_edge(prefix+parent, prefix+child)

    struct = Structure(graph, prefix+'ROOT')
    struct.getStructure()
    pickle.dump(struct, file('Structures/'+data_type+'Struct.pk', 'w'))
    pickle.dump(nameDict, file('Structures/'+data_type+'Dict.pk', 'w'))

#Used for development
def clear_tables():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM visit;")
    cursor.execute("DELETE FROM ICD_9;")
    cursor.execute("DELETE FROM code_names;")
    cursor.execute("DELETE FROM code_edges;")
    cursor.execute("DELETE FROM patient_dicts")
    cursor.execute("DELETE FROM word_indexes")
    conn.commit()

def clear_dicts():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patient_dicts")
    conn.commit()

def clear_words():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM word_indexes")
    conn.commit()