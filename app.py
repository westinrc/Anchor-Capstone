from flask import Flask, request


app = Flask('Example')

@app.route('/get-example', methods=['GET'])
def get():
    return "Hello! I just wanted to set up a quick little example of how to set up a simple REST endpoint using the Flask framework for anyone who has not done it before."

@app.route('/post-example', methods=['POST'])
def post():
    return request.data

@app.route('/put-example', methods=['PUT'])
def put():
    return request.data

@app.route('/delete-example', methods=['DELETE'])
def delete():
    return request.data

app.run()