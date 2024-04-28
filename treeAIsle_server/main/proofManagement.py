from chainDefinition import ModelBlock
from random import randint
from training_models import Model

class Contestant:
    def __init__(self,name,*args,**kwargs):
        self.name = name
        # Here performance would be calculated with a series of tests
        self.modelValues = None
        self.performance = None
        # There should be a definition of a model, performance should be calculated during the contest
    def __ge__(self,anotherContestant):
        return anotherContestant.performance < self.performance
    def train_model(self,model,trainingDataset,resultDataset,hyperValues):
        self.modelValues = model.train(trainingDataset,resultDataset,hyperValues)
    def get_performance(self,model,testDataset,resultDataset):
        self.performance = model.performance(testDataset,resultDataset)
        return self.performance[0] # 0 - loss, 1 - default seating mae
class Contest:
    def __init__(self,result_data,training_data,model,model_type='adam'):
        # Every contest has its model class, the model class should be defined in training_models.py
        self.model = model
        self.model_type = model_type
        self.result_data = result_data
        self.training_data = training_data
        self.amountOfContestants = 0
        self.contestantPointers = []
    def compare(self,chain):
        self.contestantPointers.sort(key=lambda contestant: contestant.performance, reverse=True)
        block = ModelBlock(self.contestantPointers[0].performance)
        chain.addBlock(block)
    def add_contestant(self,contestant):
        self.contestantPointers.append(contestant)
    def contest(self,iterations,test_amount):
        # Should be exchanged in the future for other dataset splitter
        from sklearn.model_selection import train_test_split
        from random import randint
        model = self.model
        training_data = self.training_data
        result_data = self.result_data
        # The split should be different
        tests = []
        for _ in range(test_amount):
            trainingData, testData, trainingResult, testResult = train_test_split(self.training_data, self.result_data, test_size=0.2,random_state=randint(1,1000))
            tests.append((testData,testResult))
        for contestant in self.contestantPointers:
            # Should send the training data and signal to train
            contestant.train_model(self.model,training_data,result_data,randint(1,10000))
        for contestant in self.contestantPointers:
            performances = []
            for iteration in range(iterations):
                performances.append(contestant.get_performance(model,tests[iteration][0],tests[iteration][1]))
            contestant.performance = sum(performances)/len(performances) # Average performance on different testsets
        # End of the contest we can compare now