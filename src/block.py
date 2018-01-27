class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_hash = str(self.index) + \
                     str(self.timestamp)[6:11].replace(" ", "") + \
                     self.previous_hash

        return block_hash

    @property
    def serialize(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous hash": self.previous_hash,
            "hash": self.hash
        }
