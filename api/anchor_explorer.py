from flask import Flask
from redis import Redis

app = Flask('anchor_explorer')
redis = Redis(host='redis', port=6379)

@app.route('/example', methods=['GET'])
def example():
    return "Hello this is an example"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)