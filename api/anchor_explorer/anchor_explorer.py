from flask import Flask, request, Response, jsonify
from redis import Redis
from utils.random_patient_generation import generate
import json

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)