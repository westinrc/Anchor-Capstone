from flask import Flask, request, Response, jsonify
#from redis import Redis
from utils.random_patient_generation import generate
from utils.settings_update import update_settings
from utils.db_func import upload_pitt_data
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)