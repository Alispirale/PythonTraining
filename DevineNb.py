from numpy import random
x = random.randint(1,101)
y=input("Devine le nombre auquel je pense")
while x!=y:
    if x<y:
        print("c'est moins coco")
        y=input("reessaye")
    if x>y:
        print("c'est plus coco")
        y=input("reessaye")
print("Bravo babe")