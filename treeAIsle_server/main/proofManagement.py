import chainDefinition as cD
from random import randint

class Contestant:
    def __init__(self,name,*args,**kwargs):
        self.name = name
        # Here performance would be calculated with a series of tests
        self.performance = randint(1,10)
        # There should be a definition of a model, performance should be calculated during the contest
    def __ge__(self,anotherContestant):
        return anotherContestant.performance < self.performance 
    
class Contest:
    def __init__(self):
        self.amountOfContestants = 0
        self.contestantPointers = []
    def compare(self,reciever,sender,amount,verifier,chain):
        self.contestantPointers.sort(key=lambda contestant: contestant.performance, reverse=True)
        block = cD.Block(reciever,sender,amount,verifier,self.contestantPointers[0].performance)
        chain.addBlock(block)
    def addContestant(self,contestant):
        self.contestantPointers.append(contestant)
