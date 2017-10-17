from flask import Flask, request, Response, jsonify
from redis import Redis
from utils.random_patient_generation import generate
from utils.settings_update import update_settings
import sys
import json
import os

app = Flask('anchor_explorer')
redis = Redis(host='redis', port=6379)
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    #settings = request.data
    #settings = update_settings(str(settings))
    #return settings

    target = os.path.join(APP_ROOT, 'settings')

    if not os.path.isdir(target):
        os.mkdir(target)
    

    settings_file = request.files['file']
    file_name = 'settings.xml'
    destination = '/'.join([target, file_name])
    settings_file.save(destination)
    sys.stderr.write(target)
    sys.stderr.write(destination)

    return request.data

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)