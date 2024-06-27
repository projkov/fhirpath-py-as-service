from flask import Flask, request, jsonify
from fhirpathpy import evaluate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/evaluate', methods=['POST'])
def evaluate_op():
    data = request.json
    resource = data.get('resource', '')
    expression = data.get('expression', [])
    result = evaluate(resource, expression, [])

    return jsonify({'data': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
