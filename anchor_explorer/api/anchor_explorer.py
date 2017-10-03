from flask import Flask, request
from redis import Redis
from ..utils.random_patient_generation import generate

app = Flask('anchor_explorer')
redis = Redis(host='redis', port=6379)

@app.route('/example', methods=['GET'])
def example():
    return "Hello this is an example"

@app.route('/generate-random-patients', methods='POST')
def generate_random_patients():
    number_patients = request.data['number_patients']
    patients_xml = generate(number_patients)
    return patients_xml

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)