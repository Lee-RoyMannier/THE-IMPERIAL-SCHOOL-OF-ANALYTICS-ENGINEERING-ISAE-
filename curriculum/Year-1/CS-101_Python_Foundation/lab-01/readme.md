# CS-101 — Practical Lab 01

## Références, mutabilité, identité

| Champ | Valeur |
|-------|--------|
| **Module** | CS-101 — Python Foundations |
| **Faculté** | I — Computer Science & Software Engineering |
| **Semestre** | Year 1 · Semester 1 |
| **Statut** | Évalué (formatif) |
| **Note de référence** | 63/100 |

---

## 🎯 Objectifs pédagogiques

À l'issue de ce lab, l'étudiant doit être capable de :

1. Expliquer le modèle d'assignation par référence de Python.
2. Distinguer identité (`is`) et égalité (`==`).
3. Différencier mutabilité et immuabilité, et leurs conséquences.
4. Expliquer le piège du mutable par défaut et le corriger.
5. Choisir entre copie superficielle et copie profonde.
6. Raisonner sur les compromis d'API (effets de bord vs fonctions pures).

## Prérequis

- Lecture 1 — Références, mutabilité, identité (complétée).

---

## 📝 Exercices

### Exercice 1 — Prédiction (fondamental)

Pour chaque snippet : **prédire la sortie sans exécuter le code**, puis vérifier mentalement avec le modèle de référence.

**1.1**
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a, b)

**1.2**
a = (1, 2, 3)
b = a
b += (4,)
print(a, b)

**1.3**
a = [1, 2]
b = a
b = b + [3]
print(a, b)

**1.4**
def mutate(d):
    d["x"] = 1

def reassign(d):
    d = {"x": 1}

data = {}
mutate(data)
print(data)
reassign(data)
print(data)

**1.5**
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a, b)

**Exercice 2 — is vs == (fondamental)
Pour chaque expression : prédire le résultat (True/False) et justifier en une phrase.**
# 2.1
[1, 2] == [1, 2]

# 2.2
[1, 2] is [1, 2]

# 2.3
x = [1, 2]
y = x
x is y

# 2.4
"abc" == "abc"

# 2.5
"abc" is "abc"

# 2.6
None == None

# 2.7
None is None

Indice pour 2.5 : les chaînes littérales courtes peuvent être internées par CPython. Est-ce une garantie du langage ou un détail d'implémentation ? Que doit-on utiliser dans du code professionnel ?

**Exercice 3 — safe_append (intermédiaire)**
Écrire une fonction safe_append(x, l=None) qui :

ajoute x à l si l est fourni ;

crée une nouvelle liste [x] si l est None ;

ne partage jamais d'état entre appels successifs sans l.

Livrables attendus :

    Docstring.

    Type hints.

    Un test pytest prouvant l'absence de partage d'état entre deux appels.

**Exercice 4 — Clones sans le module copy (intermédiaire)**
Écrire deux fonctions :

shallow_clone(lst) — copie superficielle d'une liste, sans importer copy.

deep_clone(lst) — copie profonde d'une liste imbriquée de profondeur arbitraire, sans importer copy.

Livrables attendus :

    Docstring + type hints.
    Une phrase sur la complexité temporelle et spatiale de chacune.

**Exercice 5 — Bug réel : ShoppingCart (difficile)**
class ShoppingCart:
    items = []

    def add(self, item):
        self.items.append(item)

c1 = ShoppingCart()
c2 = ShoppingCart()
c1.add("apple")
c2.add("bread")
print(c1.items)
print(c2.items)

5.1 Prédire les deux sorties. Justifier avec le modèle de référence.

5.2 Expliquer pourquoi ce bug est particulièrement dangereux en production (indice : à quel moment le bug apparaît-il ? Est-il visible dans les tests unitaires d'un seul objet ?).

5.3 Corriger le code. Écrire un test pytest qui échoue avec la version buggée et passe avec la version corrigée.

**Exercice 6 — Problème de raisonnement : design d'API**
# Version A — mutation in-place
def enrich(items: list) -> None:
    """Ajoute des métadonnées aux items, en place."""
    for item in items:
        item["enriched"] = True

# Version B — fonction pure
def enrich(items: list) -> list:
    """Retourne une nouvelle liste d'items enrichis."""
    return [{**item, "enriched": True} for item in items]

Question : laquelle recommander pour une bibliothèque publique, et pourquoi ? Discuter :

La prévisibilité pour l'appelant.

Les effets de bord (side effects).

La testabilité.

Le coût en mémoire.

Un cas où la Version A serait légitime.