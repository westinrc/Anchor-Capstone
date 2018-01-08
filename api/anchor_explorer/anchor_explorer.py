from flask import Flask, request, Response, jsonify
from redis import Redis
from utils.random_patient_generation import generate
from utils.settings_update import update_settings
import sys
import json
from mysql.connector import (connection)

app = Flask('anchor_explorer')
redis = Redis(host='redis', port=6379)

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

@app.route('/test-database', methods=['GET'])
def test_db_connection():
    cnx = connection.MySQLConnection(user='root', password='Capstone_Password',
                              host='127.0.0.1',
                              database='capstone_DB')
    return "Success!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)