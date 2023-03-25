from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    with open('./data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/<int:id>', methods=['GET'])
def get_data_by_id(id):
    with open('data.json', 'r') as f:
        data = json.load(f)
    filtered_data = [item for item in data if item['id'] == id]
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run()
