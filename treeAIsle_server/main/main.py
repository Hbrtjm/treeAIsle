import chainDefinition as cD
import proofManagement as pM


def main(*args,**kwargs):
    chain = cD.Chain(cD.Block(0,0,0,0,0))
    testContest = pM.Contest()
    contestant = pM.Contestant("B00lz")
    testContest.addContestant(contestant)
    contestant = pM.Contestant("Bruh")
    testContest.addContestant(contestant)
    testContest.compare("Andy","Jane",10,"B00lz",chain)
    testContest.compare("Andy","B0lly",100000,"B00lz",chain)
    testContest.compare("Bg","Jane",10,"B00lz",chain)
    print(chain.__str__())
    return 0
if __name__ == "__main__":
    main()
