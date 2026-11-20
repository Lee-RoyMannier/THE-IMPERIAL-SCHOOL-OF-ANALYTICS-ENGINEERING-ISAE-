**🧪 PRACTICAL LAB 3 — Fonctions, closures, décorateurs, générateurs**

**Exercice 1 — Analyse de signatures (fondamental)**

Pour chaque fonction, dites quels appels sont valides et pourquoi les autres échouent (nommez le type d'erreur). Justifiez.

python
def f(a, b=2, *args, c, **kwargs):
    return a, b, args, c, kwargs
    
**1.1 f(1, c=3)**
**1.2 f(1, 2, 3, c=4)**
**1.3 f(1, 2, c=3, d=4)**
**1.4 f(1)**
**1.5 f(a=1, c=3)**
**1.6 f(1, 2, 3, 4)**

**Exercice 2 — Prédiction : closures et late binding (fondamental)**
Prédisez la sortie sans exécuter. Justifiez le mécanisme précis.

**2.1**

python
def make_multipliers():
    return [lambda x: x * i for i in range(3)]

mults = make_multipliers()
print([m(10) for m in mults])

**2.2**

python
def make_multipliers():
    return [lambda x, i=i: x * i for i in range(3)]

mults = make_multipliers()
print([m(10) for m in mults])

**2.3**

python
def counter():
    count = 0
    def inc():
        count += 1
        return count
    return inc

c = counter()
print(c())

**2.4**

python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = counter()
print(c(), c(), c())

**Exercice 3 — Prédiction : générateurs (fondamental)**
Prédisez sans exécuter. Justifiez avec le mécanisme (exhaustion, consommation).

**3.1**

python
g = (i for i in range(3))
print(list(g))
print(list(g))

**3.2**

python
def gen():
    yield 1
    yield 2
    return 3

g = gen()
print(list(g))

**3.3**

python
def gen():
    for i in range(3):
        yield i

g = gen()
print(next(g))
print(next(g))
print(list(g))

**3.4**

python
g = (i for i in range(5))
print(2 in g)
print(list(g))

**3.5**

python
def gen():
    print("start")
    yield 1
    print("mid")
    yield 2
    print("end")

g = gen()
print("before next")
print(next(g))
print("after next")
print(next(g))

**Exercice 4 — @timed (intermédiaire)**
Écrire un décorateur @timed qui :

    Mesure le temps d'exécution de la fonction décorée.

    Affiche "{func.__name__}: {duration_ms:.2f} ms".

    Préserve les métadonnées de la fonction décorée (functools.wraps).

    Retourne la valeur de la fonction.

Contraintes :

    Docstring + type hints.

    Complexité.

    Tests pytest :

        Vérifie que la valeur retournée est intacte.

        Vérifie que func.__name__ est préservé (grâce à @wraps).

        Vérifie que le décorateur gère les exceptions (la fonction lève → l'exception propage, mais le temps est mesuré quand même).

**Exercice 5 — @retry (intermédiaire)**
Écrire un décorateur paramétré @retry(max_attempts=3, exceptions=(Exception,)) qui :

Réessaie la fonction jusqu'à max_attempts fois si elle lève une exception parmi exceptions.

Si toutes les tentatives échouent, propage la dernière exception.

Attend 0.1 × 2^attempt secondes entre les tentatives (backoff exponentiel simple).

Préserve les métadonnées.

Contraintes :

    Docstring + type hints.

    Complexité.

        Tests pytest :

        Fonction qui réussit du premier coup → 1 appel.

        Fonction qui échoue 2 fois puis réussit → 3 appels.

        Fonction qui échoue toujours → 3 tentatives puis exception.

**Exercice 6 — paginate (intermédiaire)**
Écrire un générateur paginate(iterable, page_size) qui yield des pages (listes) de taille page_size.

Exemple :

python
list(paginate(range(7), 3))  # [[0,1,2], [3,4,5], [6]]

Contraintes :

    Générateur (yield).

    Mémoire bornée : ne matérialise jamais tout l'itérable en mémoire. Doit fonctionner sur un itérable infini (itertools.count()).

    Docstring + type hints + complexité.

    Tests pytest :

        Cas nominal (7 éléments, 3 par page).

        Cas divisible exact (6 éléments, 3 par page).

        Cas avec itérable infini (itertools.islice pour limiter).

        Cas liste vide.

