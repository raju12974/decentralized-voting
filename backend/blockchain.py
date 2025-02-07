import time
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0', data={'message': 'Genesis Block'})

    def create_block(self, previous_hash, data):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': data,
            'previous_hash': previous_hash,
            'hash': self.hash_block(previous_hash, data)
        }
        self.chain.append(block)
        return block

    def hash_block(self, previous_hash, data):
        block_string = json.dumps({'previous_hash': previous_hash, 'data': data}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_block(self, data):
        previous_block = self.chain[-1]
        previous_hash = previous_block['hash']
        self.create_block(previous_hash, data)