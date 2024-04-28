import chainDefinition as cD
import proofManagement as pM
import pandas as pd
from training_models import Model
from sklearn.datasets import fetch_california_housing

def main(*args,**kwargs):
    housing_data = fetch_california_housing()
    print(housing_data)
    chain = cD.Chain(cD.Block("empty.txt",0))
    testContest = pM.Contest() 
    contestant = pM.Contestant("First_contestant")
    testContest.add_contestant(contestant)
    contestant = pM.Contestant("Second_contestant")
    testContest.add_contestant(contestant)
    testContest.contest(10,10)
    testContest.compare(chain)
    # testContest.compare("Andy","Jane",10,"test",chain)
    # testContest.compare("Andy","B0lly",100000,"test",chain)
    # testContest.compare("Bg","Jane",10,"test",chain)
    # print(chain.__str__())
    return 0
if __name__ == "__main__":
    main()
