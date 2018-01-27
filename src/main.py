import datetime as date
from block import Block
from blockchain import BlockChain
from random import *

import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request


node = Flask(__name__)

my_address = str(uuid4()).replace('-', '')
print(my_address)


def create_genesis_block():
    return Block(0, date.datetime.now(), [], "0").serialize


def new_transaction(sender, recipient, amount):
    return {
        "from": sender,
        "to": recipient,
        "amount": amount
    }


blockchain = BlockChain(create_genesis_block())


@node.route('/mine', methods=['GET'])
def mine():
    print("mining api called at: " + str(date.datetime.now()))
    block = blockchain.next_block()
    if len(block["data"]) > 0:
        blockchain.add_to_chain(block)
    return "We'll mine a new Block"


@node.route('/transactions/new', methods=['POST'])
def add_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    transaction = blockchain.new_transaction(new_transaction(values['sender'], values['recipient'], values['amount']))

    response = {'message': f'Transaction will be added to Block {transaction}'}
    return jsonify(response), 201


@node.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    node.run(host='localhost', port=8008)

