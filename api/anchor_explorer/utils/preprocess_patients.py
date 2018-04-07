import sys
import os
from multiprocessing import Pool
import string
import random
import shelve
import numpy as np 
import scipy.sparse as sparse
import cPickle as pickle
from collections import defaultdict, namedtuple
import xml.etree.ElementTree as ET
from Parsing import *
import re
from models.visit import Visit
from models.secondary_icd9 import Secondary_ICD_9
import pprint

def noRepresent(w):
    return False
    
def noDisplay(w):
    if 'bigram_' in w:
        return True
    return False

def prefix(w):
    if '_' in w:
        return w.split('_')[0]+'_'
    else:
        return ""

def process(orig_txt, prefix, datatype, display):
    if datatype == 'text':
        return parse_text(orig_txt, prefix)
    else:
        ret = []
        for t in orig_txt.split():
            try:
                ret.append({'disp':dictionaries[prefix][prefix+t], 'repr':[prefix+t]})
            except:
                ret.append({'disp':prefix+t, 'repr':[prefix+t]})
        return ret

    
def randomString(length=16):
    return "".join([random.choice(string.letters) for _ in xrange(length)])

def randomText(length=30):
    return " ".join([random.choice(words) for _ in xrange(length)])

vocab = defaultdict(int)

def represent(w, prefix):
    return (prefix+w).lower().strip(string.punctuation)

def xmlReadVisit(f):
    data = []
    l = f.readline()
    if l == "":
        return None

    if not 'visit' in l:
        print 'error parsing', l
        assert 0
    data.append(l)
    while not '</visit>' in l:
        l = f.readline()
        data.append(l)
    data = "".join(data)
    return shallow_parse_XML(data)


class real_patient_generator:
    def __init__(self, src, max_patients):
        self.input = src
        self.max_patients = max_patients
        self.n = 0
        self.f = file(self.input)
    
    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max_patients:
            pat = xmlReadVisit(self.f)
            if pat == None:
                raise StopIteration()
            self.n += 1
            return pat
        else:
            self.f.close()
            raise StopIteration()

def remove_prefix(w):
    if '_' in w:
        return w.split('_', 1)[1]
    else:
        return w

def token((disp, repr)):
    return {'disp':disp, 'repr':repr}

def realPatient(pat):
    global vocab
    
    pat['Text'] = ""
    for datum in ET.parse(settings).findall('dataTypes/datum'):
        for field in datum.findall('field'):

            try:
                content = ET.fromstring(pat[field.attrib['name']])
            except Exception, e:
                #print e
                tag = field.attrib['name']
                pat[tag] = "<"+tag+">?</"+tag+">"
                content = ET.fromstring("<"+tag+"></"+tag+">")
            tokenization = []

            for entry in content.findall(field.attrib['path']):

                txt = entry.text
                if txt == None:
                    continue

                tokenization += process(txt, datum.attrib['prefix'], datum.attrib['type'], display=None)

            if not field.attrib['name']+'_parsed' in pat:
                pat[field.attrib['name']+'_parsed'] = []

            pat[field.attrib['name']+'_parsed'] += tokenization
            pat['Text'] += "|".join(['|'.join(t['repr']) for t in tokenization]) + '|'

    
    pat['index'] = ET.fromstring(pat['index']).text

    return pat


def build_diagnosis(dictionaries, prefix, visit, all_icd9_codes_indexed):
    visit_index = visit['index']
    secondary_icd9_codes = all_icd9_codes_indexed[visit_index]

    diagnoses = []
    if (secondary_icd9_codes is not None):
        codes = [code.strip() for code in secondary_icd9_codes['codes'].split(',')]
        for code in codes:
            dictionary = {}

            try:
                dictionary['disp'] = dictionaries[prefix][prefix + code]
                dictionary['repr'] = prefix + code
            except:
                dictionary['disp'] = prefix + code
                dictionary['repr'] = prefix + code
            diagnoses.append(dictionary)
    return diagnoses


def create_patient_dict(visit, settings, dictionaries, all_icd9_codes_indexed):
    pat = {}
    padded_index = str(visit['index']).zfill(5)
    pat['index'] = 'vid_' + padded_index
    for datum in ET.parse(settings).findall('dataTypes/datum'):
        prefix = datum.attrib['prefix']
        for field in datum.findall('field'):
            field_name = field.attrib['name']

            if (not field_name + '_parsed' in pat):
                pat[field_name + '_parsed'] = []

            if (not field_name in pat):
                pat[field_name] = ''
                if field_name == 'Note':
                    note_text = visit['note_text']
                    pat[field_name] = note_text
                    remove_chars = ['\n', '\\n', '\t', '\\t']
                    for char in remove_chars:
                        note_text = note_text.replace(char, '')
                    pat_note_parsed = parse_text(note_text, prefix)
                    pat[field_name + '_parsed'] = pat_note_parsed


            if (field_name == 'Diagnosis'):
                diagnosis_parsed = build_diagnosis(dictionaries, prefix, visit, all_icd9_codes_indexed)
                pat[field_name + '_parsed'] = diagnosis_parsed
                diagnosis_string = ''
                for diagnosis in diagnosis_parsed:
                    diagnosis_string += diagnosis['repr']
                    diagnosis_string = diagnosis_string.replace('code_', ' ')
                diagnosis_string = diagnosis_string.lstrip()
                pat[field_name] = diagnosis_string

        lowered_text = visit['note_text'].lower()
        remove_chars = ['\n', '\\n', '\t', '\\t']
        split_chars = ['(', ')', '[', ']', '{', '}', '*', '.', ';', ',', ':', '-', '/']
        for char in remove_chars:
            lowered_text = lowered_text.replace(char, ' ')
        for char in split_chars:
            lowered_text = lowered_text.replace(char, ' ' + char + ' ')
 
        lowered_split_text = lowered_text.split()
        pat['Text'] = "|".join(lowered_split_text)
    return pat

def preprocess(max_patients, fix_vocab):

    # if sys.argv[1] == 'test':
    #     txt = ' '.join(sys.argv[2:])
    #     print process(txt, "", "text", None)

    
    # try:
    #     max_patients = int(sys.argv[1])
    #     xml_src = sys.argv[2] 
    #     settings = sys.argv[3]
    # except:
    #     print "usage: real_patients.py numPatients srcFile settings"
    #     sys.exit()

    settings = 'utils/icd9_settings/settings.xml'

    if 'fix_vocab' in sys.argv:
        fix_vocab = True
    else:
        fix_vocab = False

    dictionaries = {}
    for datum in ET.parse(settings).findall('dataTypes/datum'):
        if 'dictionary' in datum.attrib:
            dictionaries[datum.attrib['prefix']] = pickle.load(file(datum.attrib['dictionary']))

    anchorwords = []
    for elem in ET.parse(settings).findall('anchors'):
        anchorfile = elem.attrib['src']
        for concept in ET.parse(anchorfile).findall('.//concept'):
            anchorwords += concept.text.split('|')
    anchorwords = [z.strip() for z in set(anchorwords)]

    bigramlist = get_bigramlist()
    bigramlist += filter(lambda w: len(w.split()) > 1, anchorwords)

    sys.stdout.flush()

    realtime_prefixes = set()
    for datum in ET.parse(settings).findall('dataTypes/datum'):
        if datum.attrib['realtime'].lower() == "true":
            realtime_prefixes.add(datum.attrib['prefix'])

    visitShelf = shelve.open('visitShelf', 'n')
    wordShelf = shelve.open('wordShelf', 'n')
    visitIDs = file('visitIDs', 'w')
    visitIDs = open("visitIDs", "w")
    word_index = defaultdict(list)
    patients = []
    pool = Pool(4)

    # ******* NEW CODE ********
    visit_obj = Visit()
    all_visits = visit_obj.retrieve_all_visits()
    secondary_icd9_codes_obj = Secondary_ICD_9()
    all_icd9_codes = secondary_icd9_codes_obj.retrieve_all_ICD_9()

    all_icd9_codes_indexed = [None] * len(all_visits)
    for icd9_dict in all_icd9_codes:
        desired_index = icd9_dict['index']
        all_icd9_codes_indexed[desired_index] = icd9_dict

    x = 0
    for visit in all_visits:
        pat = create_patient_dict(visit, settings, dictionaries, all_icd9_codes_indexed)

        index = pat['index']
        for w in set(pat['Text'].split('|')):
            word_index[w].append(index)

        if (x == 1):
            print(pat)
            
            return 1
        x += 1

        print >> visitIDs, index
        patients.append(index)
        if (len(patients) % 10000):
            print(len(patients))
            sys.stdout.flush()
    visitIDs.close()


        # if (x == 1):
        #     pprint._sorted = lambda x:x
        #     pprint.pprint(pat)
        #     return 1
        # x += 1

    #for pat in pool.imap_unordered(realPatient, real_patient_generator(src=xml_src, max_patients=max_patients), chunksize=100):
    # for pat in real_patient_generator(src=xml_src, max_patients=max_patients):
    #     pat = realPatient(pat)
    #     if not fix_vocab:
    #         for w in set(pat['Text'].split('|')):
    #             if prefix(w) in realtime_prefixes:
    #                 vocab[w] += 1

    #     index = pat['index']
    #     for w in set(pat['Text'].split('|')):
    #         word_index[w].append(index)

    #     print >>visitIDs,  index
    #     patients.append(index)
    #     if len(patients) % 100 == 0:
    #         print len(patients)
    #         sys.stdout.flush()
    #visitIDs.close()

    print 'done with round 1'
    sys.stdout.flush()
    
    if not fix_vocab:
        vocab = [w for w in vocab if vocab[w] > 40]
        inv_vocab = dict(zip(vocab, xrange(len(vocab))))
    else:
        vocab,inv_vocab,_, = pickle.load(file('vocab.pk'))

    #for pat in pool.imap_unordered(realPatient, real_patient_generator(src=xml_src, max_patients=max_patients), chunksize=100):
    for n, pat in enumerate(real_patient_generator(src=xml_src, max_patients=max_patients)):
        pat = realPatient(pat)
        txt = set(pat['Text'].split('|'))
        m =  sparse.dok_matrix((1,len(vocab)))
        for w in txt:
            if w in inv_vocab:
                m[0,inv_vocab[w]] = 1
        pat['sparse_X'] = m
        index = pat['index']
        if n % 100 == 0:
            print n
            sys.stdout.flush()

        visitShelf[index] = pat
    
    print 'done with round 2'
    sys.stdout.flush()

    visitShelf.close()
    visitIDs.close()
    for w,s in word_index.items():
        try:
            wordShelf[w]=s
        except:
            print 'error', w

    wordShelf.close()
    vocab = list(vocab)
    inv_vocab = dict(zip(vocab, xrange(len(vocab))))
    display_vocab = [remove_prefix(w)+' ' for w in vocab]
    pickle.dump((vocab, inv_vocab, display_vocab), file('vocab.pk', 'w'))

