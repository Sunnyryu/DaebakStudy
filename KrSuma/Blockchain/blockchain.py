# example of what a single block looks like:

block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}

# blockchain class

import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request


class Blockchain(object):

    # default constructor
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # creates the genesis block
        self.new_block(previous_hash = '1', proof = 100)

    def new_block(self, proof, previous_hash = None):
        # creates a new block and adds it to the chain
        """
        Creates a new block in the blockchaine
        proof: <int> the proof given by the proof of work algorithm
        previous_hash: (optional) <str> hash of the previous block
        return: <dict> new block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        #reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

        pass

    def new_transaction(self, sender, recipient, amount):
        # adds a new transaction to the list of transactions
        """
        Creates a new transaction to go into the next mined block
        sender : <str> address of the sender
        recipient : <str> addres of the recipient
        amount : <int> amount
        return: <int> the index of the block that will hold this transaction

        after it adds a transaction to the list, it returns the index of the next on to be mined.
        """

        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            }
        )
        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        """
        Simple proof of work algorithm:
        - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        - p is the previous proof, and p' is the new proof
        last_proof: <int>
        return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    # With staticmethods, neither self (the object instance) nor cls (the class) is implicitly
    # passed as the first argument. They behave like plain functions except that you can call
    # them from an instance or the class:

    @staticmethod
    def hash(block):
        # hashes a block
        """
        Creates a SHA-256 hash of a block
        block: <dict> block
        return: <str>
        """
        # we must make sure that the dictionary is ordered, or else hashes are inconsistent
        block_string = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof : does has(last_proof, proof) contains 4 leading zeroes?
        last_proof: <int> previous proof
        proof: <int> current proof
        return: <bool> correct or incorrect
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    # propertymethods allows you to you do setters and getters

    @property
    def last_block(self):
        # returns the last block in the chain
        return self.chain[-1]


# instantiate our node
app = Flask(__name__)

# generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# instantiate the blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "We will mine a new block"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We will add a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # create a new transation
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be adeded to block {index}'}
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)