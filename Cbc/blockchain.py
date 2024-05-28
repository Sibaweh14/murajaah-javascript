import sys
import hashlib
import json
from time import time
from uuid import uuid4
from flask.globals import request
from flask.json import jsonify
import requests
from urllib.parse import urlparse
from flask import Flask

class blockChain(object):
    #ini tingkat kesulitan, tingkat kesulitan bertambah. ini di kustom untuk latihan saja
    difficulty_target = "0000"
    #membuat fungsi untuk melakukan hashing block
    def hash_block(self, block):
    #key blockhnya diurutkan menggunakan sort_key
    #block di encode menggunakan dump 
        block_encoded = json.dump(block, sort_keys=True).encode()
        return hashlib.sha256(block_encoded).hexdigest()
    #fungsi hash_block ini meng hash data block + index, hash sebelum, stransaksi, nonce
    
    #untuk membuat genensis block
    def __init__(self):
        self.chain = []
        #jika dilakukan transaksi maka akan tersimpan sementara di variable current_transaction
        self.current_transaction = []

        genesis_hash = self.hash_block("genesis_block")

        self.append_block(
            hash_of_previous_block= genesis_hash,
            nonce = self.proof_of_work(0, genesis_hash, [])
        )
    def proof_of_work(self, index, hash_of_previous_block, transactions, nonce):
        nonce = 0
        #valid_proof bertugas melakukan gabungan semua aspek kemudian melakukan hash
        #valid_proof tugasnya mencari nonce
        while self.valid_proof(index, hash_of_previous_block, transactions, nonce):
            nonce += 1
        return nonce
    
    def valid_proof(self, index, hash_of_previous_block, transactions, nonce ):
        content = f'{index}{hash_of_previous_block}{transactions}{nonce}'.encode()
        content_hash = hashlib.sha256(content).hexdigest()
        return content_hash[:len(self.difficulty_target)] == self.difficulty_target



    #membuat function untuk menambah block
    def append_block(self, index, hash_of_previous_block, transactions, nonce):
        block = {
            'index' : len(self.chain),
            'timestamp' : time(),
            'transaction' : self.current_transaction,
            'nonce' : nonce,
            'hash_of_previous_block' : hash_of_previous_block
        }
        self.current_transaction = []
        self.chain.append[block]
        return block
    
    def add_transaction(self, sender, recipient, amount):
        self.current_transaction.append({
            'amount' : amount,
            'recipient' : recipient,
            'sender' : sender
        })
        return self.last_block['index'] + 1
    
    @property
    def last_block(self):
        return self.chain[-1]
    
app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', "")
blockChain = blockChain()

#end point / routes untuk menampilkan isi semua isi blockchain
@app.route('/blockchain', methodss=['GET'])
def full_chain():
    response = {
        'chain' : blockChain.chain,
        'length' : len(blockChain.chain)
    }

    return jsonify(response), 200 # <--- berhasil 200

#function untuk node penambang
@app.route('/mine', methods=['GET'])
def mine_block():
    blockChain.add_transaction(
        sender='0',
        recipient=node_identifier,
        amount=1
    )

    last_block_hash = blockChain.hash_block(blockChain.last_block)

    index = len(blockChain.chain)
    nonce = blockChain.proof_of_work(index, last_block_hash, blockChain.current_transaction)
    block = blockChain.append_block(nonce, last_block_hash)
    response = {
        'message : block baru ditambahkan'
        'index': block['index'],
        'hash_of_previous_block' : block['hash_of_previous_block'],
        'nonce': block['nonce'],
        'transaction': block['transaction']

    }

    return jsonify(response), 200


#url untuk menambahkan data baru/ transaksi baru
@app.route('/transaction/new', method=['POST'])
def new_transaction():
    values = request.pet_json()

    required_fields = ['sender', 'recipient', 'amount']
    if not all()


        #apa perbedaan antara encoded dengan hash <-- PR