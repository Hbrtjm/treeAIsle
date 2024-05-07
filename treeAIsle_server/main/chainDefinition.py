import hashlib
import numpy as np

# Previous idea - to use ML as a proof of work instead of finding the best hash, but it's very limited when it reaches the local minimum,
# So it's not viable for such job and no commercial PC would handle large models which require such long chains of optimization
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
        return f"Name = {self.contestant_name}, \nMax performance = {self.maxPerformance}, \nLast Block Hash = {self.lastBlockHash}, \nHash = {self.hash_}\n\n"
    def __init__(self,contestant_name,maxPerformance,depth,,branch,model_vaules=None):
        # For now the score, or rather the "maxPerformance", is just the lowest MSE of the model on random tests. This statistically should flatten out the overfitting,
        # but is less deterministic, rather it favors the peudorandomly picked tests, further work should be done on the scoring 
        self.contestant_name = contestant_name
        self.maxPerformance = maxPerformance
        self.branch = branch
        self.depth = depth
        self.model_values = model_vaules
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


# The target "audience" would be people aiming at effectively training medium sized models - 
# such that a personal computer with a decent graphics card and a few gigs of memory could output reasonable results.
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
    def insertBlock(self,block):
        # TODO:
        # Tree-like structure feature, for now I'm using a simple hashed linked list for now. 
        # This should backtrack into a desired node and create a new descendant with a better score.  
        pass