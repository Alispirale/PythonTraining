# PythonTraining
J'ai pu aborder au travers de différents projets les concepts suivants :

**Jeu Devine Nombre :**
- La librairie Numpy
- La fonction random pour générer aléatoirement un nombre dans un intervalle
- Les bases de print
- Comment fonctionne une boucle while

**Jeu du pendu :**
- La librairie Pandas afin d'importer un tableau excel
- Comment importer un tableau excel et l'exploiter
- Comment créer une liste et l'étendre, la réduire
- Organisation du control flow avec une boucle while et des blocs if
- Utilisation d'un set à la ligne #8 afin d'unifier les éléments de la liste des lettres à trouver : cela permet de demander la lettre une seule fois à l'utilisateur même si elle est présente plusieurs fois dans le mot, selon les règles du pendu

**Jeu "rock paper scissors lizard spock" (un pierre feuille ciseaux amélioré) :**
- La librairie Pandas
- Comment créer une fonction avec def return. Cette fonction m'a permis de renvoyer le gagnant en fonction de deux élements : le choix du player 1 (ordinateur) et le choix du player 2 (humain)
- Comment exploiter un tableau excel dans un programme : j'ai inséré dans ce tableau tous les outcomes possibles d'une manche du jeu. Ainsi, chaque combinaison renvoyant à un outcome, j'ai pu le lier à la fonction créée.

**Exercie Rate Exchange :**
- Import d'un excel avec Pandas dataframe 
- Création d'un dictionnaire depuis le dataframe
- Exploitation de ce dictionnaire en associant à chaque currency un rate
- Création d'une fonction qui permet de renvoyer la valeur en USD depuis une autre currency. La fonction va chercher dans le dictionnaire la valeur (rate) correspondant à la clé indiquée (currency)
- Utilisation de la fonction try except pour vérifier que l'utilisateur entre bien un nombre valide