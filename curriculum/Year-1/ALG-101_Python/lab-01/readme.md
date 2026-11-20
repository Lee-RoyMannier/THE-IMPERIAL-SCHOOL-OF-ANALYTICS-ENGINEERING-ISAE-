# ALG-101 — Mini-labs : Algorithmes de tri

## Présentation

Cette série d'exercices a pour objectif de mettre en pratique trois algorithmes de tri fondamentaux :

- **Bubble Sort** (tri à bulles)
- **Selection Sort** (tri par sélection)
- **Insertion Sort** (tri par insertion)

Le travail est divisé en deux mini-labs :

1. Implémenter et tester les trois algorithmes.
2. Mesurer leurs performances afin d'observer concrètement leur complexité temporelle.

L'objectif n'est pas simplement d'obtenir une liste triée, mais de comprendre le fonctionnement de chaque algorithme et leurs différences de performances.

---

## Mini-lab 1 — Implémentation et tests

**Objectif :** implémenter les trois algorithmes et vérifier leur bon fonctionnement avec pytest.

### 1. Implémentation

Créer les trois fonctions suivantes :

- `bubble_sort(lst)`
- `selection_sort(lst)`
- `insertion_sort(lst)`

Pour cet exercice, recopier les implémentations présentées dans la lecture.

**Contraintes :**
- Ne pas utiliser `sorted()`.
- Ne pas utiliser `.sort()`.
- Chaque fonction doit retourner une nouvelle liste triée.
- La liste originale ne doit pas être modifiée.

### 2. Tests paramétrés avec pytest

Écrire un seul test paramétré permettant de vérifier les trois fonctions sur plusieurs cas.

| Cas | Liste d'entrée | Résultat attendu |
|---|---|---|
| Liste vide | `[]` | `[]` |
| Un élément | `[5]` | `[5]` |
| Déjà triée | `[1, 2, 3]` | `[1, 2, 3]` |
| Inversée | `[3, 2, 1]` | `[1, 2, 3]` |
| Doublons | `[3, 1, 3, 2]` | `[1, 2, 3, 3]` |

### 3. Bonus — Vérifier l'absence de mutation

Vérifier qu'aucune des trois fonctions ne modifie la liste d'origine.

Pour cela :
1. Créer une copie de la liste avant le tri avec `lst.copy()`.
2. Exécuter la fonction de tri.
3. Vérifier que la liste initiale est toujours identique à sa copie.

**Résultat attendu :** les trois fonctions retournent une liste triée sans modifier les données initiales.

---

## Mini-lab 2 — Mesurer les performances

**Durée estimée :** 15 minutes.

**Objectif :** observer empiriquement la complexité temporelle des algorithmes de tri.

### 1. Génération des données

Créer des listes contenant un nombre différent d'éléments :

| Taille | Nombre d'éléments |
|---|---:|
| Petit | 100 |
| Moyen | 500 |
| Grand | 1 000 |

Utiliser `random.sample()` pour générer des listes contenant des valeurs aléatoires et sans doublons.

### 2. Mesure du temps d'exécution

Pour chacun des trois algorithmes :

- Exécuter le tri sur les listes générées.
- Mesurer le temps avec `timeit` ou `time.perf_counter()`.
- Réaliser trois mesures indépendantes.
- Calculer la moyenne des trois mesures.

**Attention :** chaque algorithme doit recevoir une liste identique pour une même taille de données. Il ne faut pas mesurer un algorithme sur une liste déjà triée par un algorithme précédent.

### 3. Affichage des résultats

Afficher les résultats dans un tableau :

| n | Bubble Sort | Selection Sort | Insertion Sort |
|---:|---:|---:|---:|
| 100 | ... | ... | ... |
| 500 | ... | ... | ... |
| 1 000 | ... | ... | ... |

Les temps peuvent être affichés en secondes ou en millisecondes, à condition de conserver la même unité partout.

### 4. Questions d'analyse

Rédiger une réponse de 2 à 3 phrases pour chacune des questions suivantes.

**Question 1 — Évolution du temps**

Le temps d'exécution est-il multiplié approximativement par 4 lorsque la taille de la liste est multipliée par 2 ?

- Comparer les mesures obtenues.
- Expliquer le lien avec la complexité théorique en O(n²).
- Préciser que les mesures réelles peuvent varier selon la machine et les données.

**Question 2 — Insertion Sort et liste déjà triée**

Insertion Sort est-il plus rapide que Bubble Sort sur une liste déjà triée ?

- Comparer les deux algorithmes sur une liste déjà ordonnée.
- Expliquer le rôle de la condition d'arrêt anticipé de Bubble Sort.
- Expliquer pourquoi Insertion Sort effectue très peu de déplacements dans ce cas.

---

## Structure du projet

```text
ALG-101-Sorting/
│
├── README.md
│
├── sorting.py
│
├── tests/
│   └── test_sorting.py
│
└── benchmark.py
```

| Fichier | Rôle |
|---|---|
| `sorting.py` | Implémentation des trois algorithmes |
| `test_sorting.py` | Tests paramétrés et vérification de la non-mutation |
| `benchmark.py` | Mesure et comparaison des performances |
| `README.md` | Documentation du projet |

---

## Exécution

### Lancer les tests

Depuis le dossier du projet :

```bash
python -m pytest -v
```

### Lancer les benchmarks

```bash
python benchmark.py
```
