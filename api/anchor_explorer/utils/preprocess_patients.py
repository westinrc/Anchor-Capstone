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
from models.patient_dicts import Patient_dicts
from models.secondary_icd9 import Secondary_ICD_9
from models.word_indexes import Word_indexes
import pprint

def prefix(w):
    if '_' in w:
        return w.split('_')[0]+'_'
    else:
        return ""


def remove_prefix(w):
    if '_' in w:
        return w.split('_', 1)[1]
    else:
        return w


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

    settings = 'utils/icd9_settings/settings.xml'
    vocab = defaultdict(int)


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


    visitIDs = file('visitIDs', 'w')
    visitIDs = open("visitIDs", "w")
    word_index = defaultdict(list)
    patients = []
    pool = Pool(4)
    patientDicts = []


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

        if not fix_vocab:
            for w in set(pat['Text'].split('|')):
                if prefix(w) in realtime_prefixes:
                    vocab[w] += 1
        

        index = pat['index']
        for w in set(pat['Text'].split('|')):
            word_index[w].append(index)

        x += 1

        patientDicts.append(pat)

        print >> visitIDs, index
        patients.append(index)
        if (len(patients) % 10000 == 0):
            print(len(patients))
            sys.stdout.flush()
    visitIDs.close()


    print 'done with round 1'
    sys.stdout.flush()
    
    # Searches vocab dict and creates a list of words that occurred more than 40 times
    if not fix_vocab:
        vocab = [w for w in vocab if vocab[w] > 40]
        inv_vocab = dict(zip(vocab, xrange(len(vocab))))
    else:
        # Breaks, may need to add our own vocab.pk file for this to work
        vocab,inv_vocab,_, = pickle.load(file('vocab.pk'))

    for n, pat in enumerate(patientDicts):
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
        
        patient_db = Patient_dicts(n, str(pat))
        patient_db.store()



    print 'done with round 2'
    sys.stdout.flush()

    visitIDs.close()
    for word, indexes in word_index.items():
        indexes_str = ",".join(str(x) for x in indexes)
        word_index = Word_indexes(word, indexes_str)
        word_index.store()

    vocab = list(vocab)
    inv_vocab = dict(zip(vocab, xrange(len(vocab))))
    display_vocab = [remove_prefix(w)+' ' for w in vocab]
    pickle.dump((vocab, inv_vocab, display_vocab), file('vocab.pk', 'w'))
    return "Success!"



