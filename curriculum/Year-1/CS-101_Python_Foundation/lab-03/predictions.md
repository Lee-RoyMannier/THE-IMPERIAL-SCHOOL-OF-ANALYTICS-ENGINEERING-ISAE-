**1.1**
(1, 2, (), 3, {})
Explication :
- a = 1 : transmis par position.
- b = 2 : valeur par défaut.
- args = () : aucun argument positionnel supplémentaire.
- c = 3 : transmis par son nom.
- kwargs = {} : aucun argument nommé supplémentaire.

**1.2**
(1,2,(3,),4)

**1.3**
(1,2,(),3,{"d":4})
a = 1
b = 2
args = ()
c = 3
kwargs = {"d": 4}

**1.4**
a est bien renseigné et b possède une valeur par défaut.

Mais c est obligatoire

Même si *args est présent, Python ne donne pas automatiquement de valeur à c.

**1.5**
(1,2,(),3,{})
a = 1
b = 2 par défaut
args = ()
c = 3
kwargs = {}

**1.6**
Erreur car:Les arguments 3 et 4 sont récupérés dans args, car ils arrivent après b et que *args les collecte.

Python ne peut donc pas considérer le 4 comme la valeur de c

**Exercice 2**
**2.1**
À cause du late binding, les lambdas ne mémorisent pas la valeur de i au moment de leur création. Elles utilisent la valeur de i au moment de leur exécution. Comme la boucle est terminée, i vaut 2 pour les trois fonctions. Le résultat est donc [20, 20, 20].

**2.2**
Dans cette issu, le late binding est réglé car on attribut a i ca nouvelle valeur a chaque tour de boucle
[0, 10, 20]

**2.3**
error UnboundLocalError variable count car 
La variable count n'est pas locale à cette fonction. Elle appartient à la fonction extérieure.

**2.4**
Ici le bug est réglé donc affichaage 1 ensuite 2 et 3 la fin car count est stocké en mémoire

**Exercice 3**
**3.1**
Un générateur est un objet qui fournit ses éléments progressivement.
1er print => [0,1,2]
2eme print le generateur est vide donc []

**3.2**
[1,2] lors du print
Les deux yield produisent les valeurs 1 et 2.

Ensuite, le return 3 termine le générateur.

**3.3**
g stock le générateur
ensuite 1 er print, on affiche le premier yield de la boucle, ici 0
ensuite 2 eme print, on affiche le 2eme yield de la boucle, 1
Ensuite on affiche le reste du generateur, [2]

**3.4**
Python parcourt le générateur jusqu'à trouver 2.

Il consomme donc successivement :
- 0
- 1
- 2
Dès qu'il trouve 2, il renvoie True.

Mais les éléments 0, 1 et 2 ont déjà été consommés.

Il reste donc : [3,4]

**3.5**
premier print
    before next
2eme print avec le next
    start
    1
print 3
    after next
    mid
    2
en gros yield dit, on s'arrete la et on te donne la valeur et au prochain next on reprends 

**Exercice 4**


