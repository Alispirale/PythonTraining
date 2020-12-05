print('Quel est ton nom?')
monNom=input()
y=str(len(monNom))
print('Nice to meet you, '+ monNom)
print('La longueur de ton nom est de ' + y + ' caracteres') 
print('Quel est ton age?')
monAge=input()
x=int(monAge)
if x<35:
    print('Tu es jeune!')
else:
    print('Ok boomer')