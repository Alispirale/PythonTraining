import pandas as pd
df = pd.read_excel (r'MotsPendu.xlsx')
mots_liste = df["Liste"].tolist()
import random
x=random.choice(mots_liste)
for element in x:
    print("_",end=" ")
letters_to_guess=list(set([letter for letter in x]))
guessed_letters=[]
pendu=0
while len(letters_to_guess)>0 and pendu<10:
    y=input("Propose une lettre\n")
    if y in guessed_letters:
        print("Deja dit")
        pendu=pendu+1
    else:
        if y in letters_to_guess:
            guessed_letters.extend(y)
            letters_to_guess.remove(y)
            print("Bien joue")
            for element in x:
                if element in guessed_letters:
                    print(element,end=" ")
                else:
                    print ("_",end=" ")
            print()
        else:
            pendu=pendu+1
            print("Rate")
            print("Il te reste "+str(10-pendu)+" essais")
            for element in x:
                if element in guessed_letters:
                    print(element, end=" ")
                else:
                    print ("_", end=" ")
            print()
if pendu==10:
    print(f"Perdu, le mot etait {x}")
if len(letters_to_guess)==0:
    print(f"Bravo, le mot etait {x}")