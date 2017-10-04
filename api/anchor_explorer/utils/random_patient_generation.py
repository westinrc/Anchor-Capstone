import sys
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml
import string
import random
import shelve
import numpy as np 
import scipy.sparse as sparse
import pickle as pickle
from collections import defaultdict, namedtuple
import os

def randomString(length=16):
	return "".join([random.choice(string.letters) for _ in xrange(length)])

def token(disp, repr):
    return {'disp':disp, 'repr':repr}

def randomText(length=30):
    return " ".join([random.choice(words) for _ in xrange(length)])

def remove_prefix(w):
    if '_' in w:
    	return w.split('_', 1)[1]
    else:
        return w

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

random.seed(2014)
words = open(os.path.join(__location__, 'words.txt')).read().splitlines()
random.shuffle(words)
words = words[:500]
vocab = set(words)

def randomPatient():
    global vocab
    pat = {}
    pat['index'] = randomString()
    ChiefComplaint = pat['ChiefComplaint'] = randomText(2)
    TriageAssessment = pat['TriageAssessment'] = randomText(10)
    MDcomments = pat['MDcomments'] = randomText(50)
    Age = pat['Age'] = str(np.random.choice(xrange(20,80)))
    Sex = pat['Sex'] = np.random.choice(['M', 'F'])[0]
    return {'visit':pat}

def generate(n=0):
    xml_str = ""
    for _ in xrange(n):
        pat = randomPatient()
        xml = dicttoxml(pat, attr_type=False, root=False)
        dom = parseString(xml)
        pat = '\n'.join(dom.toprettyxml().split('\n')[1:])
        xml_str += pat
    return xml_str
