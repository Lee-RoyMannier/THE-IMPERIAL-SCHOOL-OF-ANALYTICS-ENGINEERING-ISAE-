**Exercice 1 — Analyse de complexité (fondamental)**

Pour chaque snippet : donnez la complexité temporelle en notation Big O (en fonction de n = len(lst) ou len(d)), et justifiez en une phrase avec la complexité des opérations élémentaires.

**1.1**

python
def f(lst):
    return lst[0]
**1.2**

python
def f(lst):
    return lst[-1]
**1.3**

python
def f(lst, x):
    return x in lst
**1.4**

python
def f(s, x):
    return x in s    # s est un set
**1.5**

python
def f(d, k):
    return k in d    # d est un dict
**1.6**

python
def f(lst, x):
    return lst.count(x)
**1.7**

python
def f(lst):
    return lst.pop(0)
**1.8**

python
def f(lst):
    return lst[-1]
**1.9**

python
def f(d, k):
    return d.get(k, 0)
**1.10**

python
def f(a, b):
    return list(set(a) & set(b))    # a, b sont des listes

**Exercice 2 — Prédiction (fondamental)**
Prédisez la sortie sans exécuter. Justifiez en une phrase.

**2.1**

python
d = {}
d[1] = "a"
d[2] = "b"
d[3] = "c"
print(list(d.keys()))
**2.2**

python
s = {3, 1, 2, 1, 3}
print(len(s))
**2.3**

python
t = (1, [2, 3])
print(hash(t))
**2.4**

python
s = set()
s.add([1, 2])
print(s)
**2.5**

python
d = {"a": 1, "b": 2}
for k in d:
    if k == "a":
        del d[k]
print(d)


**Exercice 3 — deduplicate (intermédiaire)**
Écrire deduplicate(lst) qui :

    Retourne une liste sans doublons.

    Préserve l'ordre d'apparition des éléments.

    Complexité O(n).

Contraintes :

    Docstring + type hints.

    Justifier pourquoi un set seul ne suffit pas (indice : ordre d'itération).

    Tests pytest : cas nominal, liste vide, liste de doublons complets.

    Complexité temporelle et spatiale.

**Exercice 4 — two_sum (intermédiaire)**
Écrire two_sum(lst, target) qui retourne les indices de deux éléments dont la somme vaut target, ou None si aucune paire n'existe.

Contraintes :

    Complexité O(n).

    Docstring + type hints.

    Justifier pourquoi une approche naïve est O(n²) et pourquoi la vôtre est O(n).

    Tests pytest : cas nominal, cas sans solution, cas avec doublons.

    Bonus : que se passe-t-il si plusieurs paires existent ? Documenter le choix.

**Exercice 5 — Bug réel : UserIndex (difficile)**
Considérez ce code :

python
class UserIndex:
    def __init__(self):
        self.users = []

    def add(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def get(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                return u
        return None

**5.1** Quelle est la complexité de get en fonction de n = len(self.users) ? Justifiez.

**5.2** Réécrivez UserIndex pour que get soit O(1) moyen. Quelle structure utiliser, et pourquoi ?

**5.3** Quel est le compromis de votre nouvelle implémentation (indice : mémoire, ordre, mutation) ?

**5.4** Écrire un test pytest qui vérifie que get est sensiblement plus rapide avec votre version qu'avec la version naïve, sur un grand n. Utilisez time.perf_counter. Documenter la différence observée.

**Exercice 6 — Design judgment : choix de structure (difficile, sans code obligatoire)
Vous devez concevoir une bibliothèque qui gère une file d'attente de tâches avec les opérations suivantes :

    enqueue(task) — ajouter une tâche en fin de file.

    dequeue() — retirer la tâche en tête de file.

    contains(task) — tester si une tâche est dans la file.

    size() — nombre de tâches dans la file.

Questions :

**6.1** Quelle(s) structure(s) de données utilisez-vous ? Justifiez par la complexité de chaque opération.

**6.2** Que se passe-t-il si vous utilisez une list pour dequeue ? Quelle est la complexité ? Proposez une alternative.

**6.3** Comment gérez-vous le cas où contains doit être O(1) et que les tâches ne sont pas hashables par défaut ? Proposez une stratégie (indice : __hash__ / __eq__, ou structure auxiliaire).

**6.4** Si plusieurs tâches ont la même priorité, faut-il garantir l'ordre FIFO ? Comment ?

**6.5** Décrivez un compromis que vous devez trancher, et votre décision.

Pas de code obligatoire — c'est la justification qui compte. Un diagramme textuel ou un tableau est acceptable.