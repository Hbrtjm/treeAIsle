import hashlib
import numpy as np

class Block:
    def __str__(self):
        return f"Max performance = {self.maxPerformance}, Transaction Reciever = {self.reciever}, Transaction Sencer = {self.sender}, Transaction Verifier = {self.verifier}, Last Block Hash = {self.lastBlockHash}, Last Block Pointer = {self.lastBlock}, Hash = {self.hash_}\n"
    def __init__(self,reciever,sender,amount,verifier,maxPerformance):
        self.maxPerformance = maxPerformance
        self.reciever = reciever
        self.sender = sender
        self.verifier = verifier
        self.lastBlockHash = None
        self.lastBlock = None
        self.hash_ = None
    def getHash(self):
        return self.hash_
    def createBlock(self,lastBlock):
        self.lastBlockHash = lastBlock.getHash()
        self.lastBlock = lastBlock
        hasher = hashlib.sha256()
        hasher.update(np.random.bytes(10))
        hasher.update(self.reciever)
        hasher.update(self.sender)
        hasher.update(self.amount)
        hasher.update(self.verifier)
        hasher.update(self.maxPerformance)
        hasher.update(self.lastBlockHash)
        hasher.update(lastBlock)
        self.hash_ = hasher.hexdigest()
        return self

class ModelBlock:
    def __str__(self):
        return f"Max performance = {self.maxPerformance}, Transaction Reciever = {self.reciever}, Transaction Sencer = {self.sender}, Transaction Verifier = {self.verifier}, Last Block Hash = {self.lastBlockHash}, Last Block Pointer = {self.lastBlock}, Hash = {self.hash_}\n"
    def __init__(self,model_filename,maxPerformance):
        self.maxPerformance = maxPerformance
        self.model_filename = model_filename
        self.lastBlockHash = None
        self.lastBlock = None
        self.hash_ = None
    def getHash(self):
        return self.hash_
    def createBlock(self,lastBlock):
        self.lastBlockHash = lastBlock.getHash()
        self.lastBlock = lastBlock
        hasher = hashlib.sha256()
        hasher.update(np.random.bytes(10))
        # hasher.update(self.maxPerformance)
        # hasher.update(self.model_filename)
        # hasher.update(self.lastBlockHash)
        # hasher.update(self.lastBlock)
        self.hash_ = hasher.hexdigest()
        return self

class Chain:
    def __str__(self):
        main_string = ""
        main_string += f"Chain ID: 0\n"
        currentBlock = self.headBlock
        while not currentBlock is None:
            main_string += currentBlock.__str__()
            currentBlock = currentBlock.lastBlock
        return main_string
    def __init__(self,startingBlock):
        self.startingBlock = startingBlock
        self.chainSize = 0
        # self.id = get from database and increment 
        self.headBlock = startingBlock
    def addBlock(self,block):
        self.chainSize += 0
        oldHeadBlock = self.headBlock
        self.headBlock = block.createBlock(oldHeadBlock)
