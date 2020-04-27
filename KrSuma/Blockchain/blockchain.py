"""
Example of what a single block looks like:

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
"""

# blockchain class

import hashlib
import json
import requests
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
from urllib.parse import urlparse


class Blockchain(object):

    # default constructor
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()

        # creates the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
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

        # reset the current list of transactions
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
        block_string = json.dumps(block, sort_keys=True).encode()
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

    """Consensus"""

    def register_node(self, address):
        """
        Add a new node to the list of nodes
        address: <str> address of node.
        return: none
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        """
        Determine if a given blockchai is valid
        chain: <list> blockchain
        return: <bool> true if valid, false if not
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")

            # check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False
            # check that the proof of work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflict(self):
        """
        This is the Consensus Algorithm.
        Resolves the conflict by replacing our chain with the longest one in the network.
        return: <bool> true if our chain was replaces, False if not.
        """
        neighbours = self.nodes
        new_chain = None

        # look for chains longer than ours
        max_length = len(self.chain)

        # grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # replace our chain if we discoverd a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False


"""Our blockchain as an API"""

# instantiate our node
app = Flask(__name__)

# generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# instantiate the blockchain
blockchain = Blockchain()


# create the /mine endpoint, which is a GET request.
@app.route('/mine', methods=['GET'])
def mine():
    return "We will mine a new block"


# create the /transactions/.new endpoint, which is a POST request, since we will be sending data to it.
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We will add a new transaction"


# create the /chain endpoint, which returns the full blockchain
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


""" The transaction endpoint """


# a method for creating transactions
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


""" The mining endpoint"""


# calculate proof of work
# reward the miner by adding a trasaction granting us 1 coin
# for the new block by adding it to the chain


@app.route('/mine', methods=['GET'])
def mine():
    # run the proof of work algorithm to get the next proof:
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # receive a reward for finding the proof
    # sender is 0 to signify that this node has mined a new coin
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1
    )

    # forget the new block y addin it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'New Block Forged',
        'index': block['index'],
        'transactions:': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response, 200)


""" Consensus nodes """


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error - nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Chain replaced',
            'new_chain': blockchain.chain
        }
    else:
        reponse = {
            'message': 'Chain is authoritative',
            'chain': blockchain.chain
        }
    return jsonify(response), 200


"""MAIN"""

# runs the server on port 5000
if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=5000)
