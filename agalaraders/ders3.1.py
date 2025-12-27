import time
import json

def fact(x):
    if x<=0:
        return 1
    return x * fact(x-1)

def factsqr(LIST):
    data = {
        "Number": [],
        "Factorial": [],
        "Double_Factorial": []
    }

    for currentNumber in LIST:
        data["Number"].append(int(currentNumber))
        data["Factorial"].append(fact(int(currentNumber)))
        data["Double_Factorial"].append(fact(fact(int(currentNumber))))
    return data


userData = factsqr(list((tuple(input()))))

with open("doubleFactorialData.json","w",encoding="utf-8") as openJson:
    json.dump(userData,openJson,indent=4,ensure_ascii=False)