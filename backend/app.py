from flask import Flask, jsonify, request
from blockchain import Blockchain
from redis_db import get_candidates, add_candidate, redis_client
import config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain = blockchain.chain
    return jsonify(chain), 200

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    required_fields = ['voter_id', 'candidate_id']

    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing fields'}), 400

    voter_id = data['voter_id']
    candidate_id = data['candidate_id']

    if redis_client.get(voter_id):
        return jsonify({'message': 'Already voted'}), 400

    redis_client.set(voter_id, candidate_id)
    blockchain.add_block({'voter_id': voter_id, 'candidate_id': candidate_id})

    return jsonify({'message': 'Vote recorded'}), 201

@app.route('/candidates', methods=['GET'])
def candidates():
    return jsonify(get_candidates())

@app.route('/add-candidate', methods=['POST'])
def add_new_candidate():
    data = request.get_json()
    required_fields = ['name']

    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing fields'}), 400
    
    response = add_candidate(data['name'])

    if 'error' in response:
        return jsonify({'message': response['error']}), 400

    return jsonify({'message': 'Candidate added'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)