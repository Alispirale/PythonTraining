from numpy import random
x = random.randint(1,101)
y = input("Devine le nombre auquel je pense")
while x!=y:
    if x<y:
        print("C'est moins !")
        y = input("Reessaye")
    if x>y:
        print("C'est plus !")
        y=input("Reessaye")
print("Bravo !")