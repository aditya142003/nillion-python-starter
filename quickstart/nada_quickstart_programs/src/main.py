from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    govt = Party(name="Govt")

    tenderAmtA = SecretInteger(Input(name="A", party=party1))
    tenderAmtB = SecretInteger(Input(name="B", party=party2))

    condition = tenderAmtA > tenderAmtB
    minimum = condition.if_else(tenderAmtA, tenderAmtB)

    return [Output(minimum, "minimum tender", govt)]