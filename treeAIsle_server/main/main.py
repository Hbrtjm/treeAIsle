import chainDefinition as cD
import proofManagement as pM
import pandas as pd
from training_models import Model
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler

def main(*args,**kwargs):
    data = fetch_california_housing()
    chain = cD.Chain(ModelBlock("empty.txt",0))
    X = pd.DataFrame(data.data, columns=data.feature_names)
    print(X.shape)
    y = data.target
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = Model()
    testContest = pM.Contest(X_scaled,y,model) 
    contestant = cD.Contestant("First_contestant")
    testContest.add_contestant(contestant)
    contestant = cD.Contestant("Second_contestant")
    testContest.add_contestant(contestant)
    testContest.contest(3,2)
    testContest.compare(chain)
    print(chain.__str__())
    return 0
if __name__ == "__main__":
    main()