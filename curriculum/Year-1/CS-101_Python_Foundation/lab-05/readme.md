# 🏛️ ISAE — CS-101 | Lecture 5
## Dataclasses & Typing — Remplacer les dictionnaires par des objets typés

## 🎯 Objectif pédagogique

Cette série d'exercices a pour objectif de mettre en pratique les `dataclasses` et les annotations de types (`typing`) en Python.

L'objectif est de passer d'une manipulation de données sous forme de dictionnaires à une structure orientée objet, plus lisible, mieux organisée et plus facile à maintenir.

Les exercices s'appuient sur le travail réalisé lors de la Lecture 4 : l'analyse et l'agrégation de transactions.

---

# 📁 Structure du projet

```text
lecture-05/
│
├── lab.py
│
├── transactions.csv
│
├── tests/
│   ├── __init__.py
│   ├── test_summarize.py
│   └── test_load_transactions.py
│
└── README.md
```

---

# 🧪 Mini-lab 1 — Refactoriser summarize avec des dataclasses

**Durée estimée : 15 minutes**

## Objectif

Refactoriser la fonction `summarize` de la Lecture 4 pour remplacer les dictionnaires par des objets typés.

Le programme doit représenter les transactions et le résultat de l'analyse à l'aide de deux dataclasses.

## 1. Dataclass Transaction

Créer une dataclass `Transaction` contenant les attributs suivants :

| Attribut | Type | Description |
|---|---|---|
| `id` | `int` | Identifiant de la transaction |
| `amount` | `float` | Montant de la transaction |
| `category` | `str` | Catégorie de la transaction |
| `transaction_date` | `str` | Date de la transaction |

## 2. Dataclass Summary

Créer une dataclass `Summary` contenant :

| Attribut | Type | Valeur initiale |
|---|---|---|
| `total` | `float` | `0.0` |
| `by_category` | `dict[str, float]` | Dictionnaire vide |
| `count` | `int` | `0` |
| `biggest` | `Transaction \| None` | `None` |

**Contrainte :** utiliser `field(default_factory=dict)` pour initialiser `by_category`.

## 3. Fonction summarize

Réécrire la fonction avec la signature suivante :

```python
def summarize(transactions: list[Transaction]) -> Summary:
    ...
```

La fonction doit :

- Calculer le montant total de toutes les transactions.
- Calculer le montant total par catégorie.
- Compter le nombre de transactions.
- Identifier la transaction ayant le montant le plus élevé.
- Retourner un objet `Summary`.
- Gérer correctement une liste vide.
- Parcourir les transactions en un seul passage.

**Contraintes de qualité :**

- Ajouter une docstring.
- Ajouter les annotations de types.
- Ne pas utiliser plusieurs parcours pour calculer les statistiques.
- Utiliser les attributs des objets (`transaction.amount`) et non des accès par clés (`transaction["amount"]`).

## 4. Tests pytest

Créer au minimum deux tests.

### Test 1 — Cas nominal

Utiliser le jeu de cinq transactions suivant :

| ID | Montant | Catégorie | Date |
|---:|---:|---|---|
| 1 | 42.50 | food | 2026-01-03 |
| 2 | 180.00 | travel | 2026-01-03 |
| 3 | 12.00 | food | 2026-01-04 |
| 4 | 250.00 | tech | 2026-01-04 |
| 5 | 75.00 | food | 2026-01-05 |

Résultats attendus :

| Indicateur | Résultat |
|---|---:|
| Total | 559.5 |
| Food | 129.5 |
| Travel | 180.0 |
| Tech | 250.0 |
| Nombre de transactions | 5 |
| Plus grosse transaction | ID 4 |

### Test 2 — Première transaction maximale

Créer un jeu de transactions dans lequel la première transaction possède le montant le plus élevé.

Vérifier que la fonction identifie correctement cette première transaction comme étant la plus grosse.

**Objectif du test :** vérifier que l'initialisation de `biggest` fonctionne correctement, même lorsque la première transaction est déjà le maximum.

---

# 🧪 Mini-lab 2 — Charger des transactions depuis un CSV

**Durée estimée : 15 minutes**

## Objectif

Créer une fonction capable de lire un fichier CSV et de transformer ses lignes en objets `Transaction`.

Cet exercice rapproche le travail réalisé en Python d'un cas concret de traitement de données.

## 1. Fichier CSV

Créer un fichier `transactions.csv` contenant les colonnes suivantes :

```csv
id,amount,category,date
1,42.50,food,2026-01-03
2,180.00,travel,2026-01-03
3,12.00,food,2026-01-04
4,250.00,tech,2026-01-04
```

## 2. Fonction load_transactions

Créer une fonction avec la signature suivante :

```python
def load_transactions(path: str) -> list[Transaction]:
    ...
```

La fonction doit :

- Ouvrir et lire le fichier CSV.
- Utiliser `csv.DictReader` ou `csv.reader`.
- Transformer chaque ligne en objet `Transaction`.
- Convertir `id` en `int`.
- Convertir `amount` en `float`.
- Conserver `category` et `date` sous forme de chaînes de caractères.
- Retourner une liste de transactions.
- Retourner une liste vide si le fichier ne contient aucune ligne de données.

**Contraintes de qualité :**

- Utiliser uniquement les bibliothèques standard de Python.
- Ajouter une docstring.
- Ajouter les annotations de types.
- Gérer correctement la fermeture du fichier.

## 3. Tests pytest

Créer au minimum deux tests.

### Test 1 — Chargement d'un fichier temporaire

Utiliser la fixture `tmp_path` de pytest pour créer un fichier CSV temporaire.

Vérifier :

- Que le fichier est correctement lu.
- Que le nombre de transactions est correct.
- Que les lignes sont transformées en objets `Transaction`.
- Que les conversions de types sont correctes (`int` et `float`).
- Que les attributs contiennent les bonnes valeurs.

### Test 2 — Fichier vide

Créer un fichier CSV contenant uniquement l'en-tête :

```csv
id,amount,category,date
```

Vérifier que la fonction retourne :

```python
[]
```

---

# 🧠 Question de réflexion — frozen=True

Répondre en deux ou trois phrases :

**Pourquoi `Transaction` pourrait-elle être un bon candidat pour `@dataclass(frozen=True)` ? Existe-t-il une contre-indication ?**

Piste de réflexion :

Une transaction représente un événement enregistré. Mais imaginons qu'une erreur soit détectée après sa création et que l'on souhaite modifier son montant :

```python
transaction.amount = 150.0
```

Que se passerait-il si la dataclass était gelée avec `frozen=True` ?

Réfléchir aux avantages et aux limites de l'immuabilité dans ce contexte.

---

# ⚙️ Compétences travaillées

| Compétence | Notions |
|---|---|
| Programmation orientée objet | Classes et instances |
| Dataclasses | `@dataclass`, attributs, méthodes générées |
| Valeurs par défaut | `field(default_factory=...)` |
| Immutabilité | `frozen=True` |
| Typage Python | `list[T]`, `dict[K, V]`, `T \| None` |
| Traitement de données | Lecture et conversion CSV |
| Génération de tests | pytest, `tmp_path` |
| Algorithmique | Agrégation en un seul passage |
| Qualité du code | Docstrings et annotations de types |

