print('Quel est ton nom ?')
monNom = input()
print('Nice to meet you, ' + monNom)
print('La longueur de ton nom est de ' + str(len(monNom)) + ' caracteres') 
print('Quel est ton age ?')
monAge = input()
if int(monAge)<35:
    print('Tu es jeune !')
else:
    print('Ok boomer')