import datetime as date
from block import Block


class BlockChain:

    def __init__(self, genesis_block):
        self.chain = [genesis_block]
        self.current_transactions = []

    def add_to_chain(self, new_block):
        self.chain.append(new_block)
        self.current_transactions = []

    def next_block(self):
        new_index = len(self.chain)
        timestamp = date.datetime.now()
        data = list(self.current_transactions)
        previous_hash = self.last_block["hash"]

        return Block(new_index, timestamp, data, previous_hash).serialize

    def new_transaction(self, transaction):
        self.current_transactions.append(transaction)

    @property
    def last_block(self):
        return self.chain[-1]

    def describe_block(self):
        print("Blockchain Description \n")
        for block in self.chain:
            print("Block " + str(block.index))
            print("Timestamp: " + str(block.timestamp))

            print("Transactions: ")
            for item in block.data:
                print(item)
            print()

            print("Hash: " + block.hash)
            print()
