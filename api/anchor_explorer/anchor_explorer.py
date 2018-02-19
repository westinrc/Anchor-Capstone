from flask import Flask, request, Response, jsonify
from utils.random_patient_generation import generate
from utils.settings_update import update_settings
from utils.data_storage import upload_pitt_data
from utils.data_storage import load_icd9_structure
from utils.data_storage import build_structured_rep
from utils.preprocess_patients import preprocess
import sys
import json
import pymysql

app = Flask('anchor_explorer')
#redis = Redis(host='redis', port=6379)

@app.route('/example', methods=['GET'])
def example():
    return "Hello this is an example"

@app.route('/generate-random-patients', methods=['POST'])
def generate_random_patients():
    request_json = request.get_json(force=True)
    number_patients = request_json['number_patients']
    patients_xml = generate(number_patients)
    return Response(patients_xml, mimetype='text/xml')

@app.route('/update-settings', methods=['PUT'])
def settings_update():
    settings = request.data
    settings = update_settings(str(settings))
    return settings

@app.route('/upload-pitt-delimited', methods=['POST'])
def fill_database():
    pitt_file = request.files.get('pitt-delimited')
    result = upload_pitt_data(pitt_file)
    return result

@app.route('/load-icd9-structure', methods=['POST'])
def load_icd9_struct():
    load_icd9_structure()
    return "Success"

@app.route('/build-structured-rep', methods=['POST'])
def build_rep():
    request_json = request.get_json(force=True)
    data_type = request_json['datatype']
    build_structured_rep(data_type)
    return "Success"

@app.route('/preprocess-patients', methods=['POST'])
def preprocess_patients():
    request_json = request.get_json(force=True)
    max_patients = request_json['max_patients']
    preprocess(max_patients)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)