from hashlib import sha256
import numpy as np

# Previous idea - to use ML as a proof of work instead of finding the best hash, but it's very limited when it reaches the local minimum,
# So it's not viable for such job and no commercial PC would handle large models which require such long chains of optimization
class Block():
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
        hasher = sha256()
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

class ModelBlock():
    def __str__(self):
        return f"Name = {self.contestant_name}, \nMax performance = {self.maxPerformance}, \nLast Block Hash = {self.lastBlockHash}, \nHash = {self.hash_}\n\n"
    def __init__(self,contestant_name,maxPerformance,depth,branch,chain_id,model_values_filename=None):
        # For now the score, or rather the "maxPerformance", is just the lowest MSE of the model on random tests. This statistically should flatten out the overfitting,
        # but is less deterministic, rather it favors the peudorandomly picked tests, further work should be done on the scoring 
        self.contestant_name = contestant_name
        self.maxPerformance = maxPerformance
        self.branch = branch
        self.depth = depth
        self.model_values_filename = model_values_filename
        self.lastBlockHash = None
        self.lastBlock = None
        self.chain_id = chain_id
        if self.depth == 0:
            hasher = sha256()
            hasher.update(np.random.bytes(10))
            # hasher.update(self.chain_id)
            self.hash_ = hasher.hexdigest()
        else:
            self.hash_ = None # It will be determined by the contest in createBlock
    def getHash(self):
        return self.hash_
    def createBlock(self,lastBlock):
        self.lastBlockHash = lastBlock.getHash()
        self.lastBlock = lastBlock
        hasher = sha256()
        hasher.update(np.random.bytes(10))
        # hasher.update(self.maxPerformance)
        # hasher.update(self.model_values_filename)
        # hasher.update(self.lastBlockHash)
        # hasher.update(self.chain_id)
        # hasher.update(self.lastBlock)
        self.hash_ = hasher.hexdigest()
        return self


# The target "audience" would be people aiming at effectively training medium sized models - 
# such that a personal computer with a decent graphics card and a few gigs of memory could output reasonable results.
class Chain():
    def __str__(self):
        main_string = ""
        main_string += f"Chain ID: 0\n"
        currentBlock = self.headBlock
        while not currentBlock is None:
            main_string += currentBlock.__str__()
            currentBlock = currentBlock.lastBlock
        return main_string
    def __init__(self,startingBlock,chain_id):
        self.startingBlock = startingBlock
        self.chainSize = 0
        self.chain_id = chain_id
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


def get_chain_id():
    # Should give us a last pointer for chain ID from database
    return randint(1,10000)

# An alternative to consider
# 
# from tensorflow import keras
# class MyModel(keras.Model):
#     def __init__(self):
#         super().__init__()
#         self.dense1 = keras.layers.Dense(32, activation="relu")
#         self.dense2 = keras.layers.Dense(5, activation="softmax")
#         self.dropout = keras.layers.Dropout(0.5)

#     def call(self, inputs, training=False):
#         x = self.dense1(inputs)
#         x = self.dropout(x, training=training)
#         return self.dense2(x)

# model = MyModel()
class Model():
    def __init__(self,model_type='adam',layers_sizes=[10,10,1],layers_functions=['relu','relu','output'],metrics=['mean_absolute_error'],loss_function = 'mean_squared_error',activation_functions = ['relu','relu','output'],library='tensorflow'):
        self.model_type = model_type
        self.model = None
        self.library = library
        self.layers_sizes = layers_sizes
        self.layer_functions = layers_functions
        self.loss_function = loss_function
        self.metrics = metrics
        self.activation_functions = activation_functions
    def train(self,trainingDataset, resultDataset, epochs, chain_id, current_hash, checkpoint_directory, chain, hypervaules):
        if self.library == 'tensorflow': # Generally that's not the way, it's for demonstration purposes
            # try:
            import tensorflow as tf
            layers_sizes = self.layers_sizes
            optimizer = self.model_type
            metrics = self.metrics
            layer_functions = self.layer_functions
            activation_functions = self.activation_functions
            loss_function = self.loss_function
            
            # Define a TensorFlow model
            model_table = []
            print(trainingDataset.shape)
            model_table.append(tf.keras.layers.Dense(layers_sizes[0],activation=activation_functions[0],input_shape=(trainingDataset.shape[1],)))
            for i in range(1,len(layers_sizes)):
                if activation_functions[i] == 'output':
                    model_table.append(tf.keras.layers.Dense(layers_sizes[i]))
                else:
                    model_table.append(tf.keras.layers.Dense(layers_sizes[i],activation=layer_functions[i]))
            self.model = tf.keras.Sequential(model_table)
            self.model.compile(optimizer=optimizer, loss=loss_function, metrics=metrics)
            self.model.summary()
            if chain.headBlock.depth > 0:
              chekcpoint_path = f"{checkpoint_directory}{chain.chain_id},{chain.headBlock.lastBlock.hash_}"
              self.model.load_weights(chekcpoint_path)
            current_hash = chain.headBlock.hash_
            checkpoint_path = f"{checkpoint_directory}{chain_id},{current_hash}" # {branch}"
            callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path, save_weights_only=True, verbose=1)
            print(f"{trainingDataset.shape[0]} {resultDataset.shape[0]}")
            history = self.model.fit(trainingDataset, resultDataset, epochs=epochs, validation_split=0.1,callbacks=[callback])
            return self.model
            # except Exception as e:
            #     print(f"An exception occurred during model training {e}")
    def performance(self,testData,testResult):
        # try:
        #     # Evaluate the model    
        if self.library == 'tensorflow':
            import tensorflow as tf
            test_loss, test_mae = self.model.evaluate(testData, testResult)
            return (test_loss, test_mae)
        else: # As the project grows, we can add more models here, however the whole structure seems a bit inefficient
            print("Unknown model")
            raise ValueError("Unknown models")
        # except Exception as e:
        #     print(f"An exception occurred during model verification {e}")

from random import randint

class Contestant():
    def __init__(self,name,*args,**kwargs):
        self.name = name
        # Here performance would be calculated with a series of tests
        self.modelValues = None
        self.performance = None
        # There should be a definition of a model, performance should be calculated during the contest
    def __ge__(self,anotherContestant):
        return anotherContestant.performance < self.performance
    def train_model(self,model,trainingDataset,resultDataset,epochs,chain_id,current_block, checkpoint_directory, chain ,hyperValues):
                               #       trainingDataset, resultDataset, epochs, chain_id, current_hash, checkpoint_directory, hypervaules
        self.modelValues = model.train(trainingDataset,resultDataset,epochs,chain_id,current_block, checkpoint_directory, chain ,hyperValues)
    def get_performance(self,model,testDataset,resultDataset):
        self.performance = model.performance(testDataset,resultDataset)
        try:
          return self.performance[0] # 0 - loss, 1 - default seating mae
        except Exception as e:
          print(e)
class Contest():
    def __init__(self,training_data,result_data,model,model_type='adam'):
        # Every contest has its model class, the model class should be defined in training_models.py
        self.model = model
        self.model_type = model_type
        self.result_data = result_data
        self.training_data = training_data
        self.amountOfContestants = 0
        self.contestantPointers = []
    def compare(self,chain):
        self.contestantPointers.sort(key=lambda contestant: contestant.performance, reverse=True)
        block = ModelBlock(self.contestantPointers[0].name,self.contestantPointers[0].performance,chain.headBlock.depth+1,0,chain.chain_id,f"{chain.chain_id},{chain.headBlock.hash_}")
        chain.addBlock(block)
    def add_contestant(self,contestant):
        self.contestantPointers.append(contestant)
    def contest(self,epochs,test_amount,chain):
        # Should be exchanged in the future for other dataset splitter
        from sklearn.model_selection import train_test_split
        from random import randint
        model = self.model
        training_data = self.training_data
        result_data = self.result_data
        checkpoint_directory = "./saved_vaules/"
        # The split should be different
        tests = []
        for _ in range(test_amount):
            trainingData, testData, trainingResult, testResult = train_test_split(training_data, result_data, test_size=0.2,random_state=randint(1,1000))
            tests.append((testData,testResult))
        for contestant in self.contestantPointers:
            # Should send the training data and signal to train
            contestant.train_model(model,trainingData,trainingResult,epochs, chain.chain_id, chain.headBlock.hash_ , checkpoint_directory, chain ,randint(1,10000))
        for contestant in self.contestantPointers:
            performance = 0
            for test_iteration in range(test_amount):
                performance += contestant.get_performance(model,tests[test_iteration][0],tests[test_iteration][1])
            contestant.performance = performance/test_amount # Average performance on different testsets
        # End of the contest we can compare now

import pandas as pd
from sklearn.datasets import fetch_california_housing, load_iris
from sklearn.preprocessing import StandardScaler

def main(*args,**kwargs):
    # data = fetch_california_housing()
    data = load_iris()
    new_chain_id = get_chain_id()
    chain = Chain(ModelBlock(None,0,0,0,new_chain_id),new_chain_id)
    X = pd.DataFrame(data.data, columns=data.feature_names)
    print(X.shape)
    y = data.target
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = Model()
    testContest = Contest(X_scaled,y,model) 
    contestant = Contestant("First_contestant")
    testContest.add_contestant(contestant)
    contestant = Contestant("Second_contestant")
    testContest.add_contestant(contestant)
    testContest.contest(3,2,chain)
    testContest.compare(chain)    
    print("Done first training")
    testContest.contest(3,2,chain)
    testContest.compare(chain)
    testContest.contest(3,2,chain)
    testContest.compare(chain)
    testContest.contest(3,2,chain)
    testContest.compare(chain)
    testContest.contest(3,2,chain)
    testContest.compare(chain)
    testContest.contest(3,2,chain)
    testContest.compare(chain)
    testContest.contest(3,2,chain)
    testContest.compare(chain)
    testContest.contest(3,2,chain)
    testContest.compare(chain)
    testContest.contest(3,2,chain)
    testContest.compare(chain)
    print(chain.__str__())
    return 0
if __name__ == "__main__":
    main()  