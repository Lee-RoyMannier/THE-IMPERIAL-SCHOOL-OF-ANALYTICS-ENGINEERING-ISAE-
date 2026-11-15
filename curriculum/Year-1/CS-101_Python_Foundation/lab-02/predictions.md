# CS-101 — Lab 02 — Analyse

## Exercice 1 — Complexités

| # | Complexité | Justification |
|:-:|:----------:|---------------|
| 1.1 | O(1) | Accès direct par index, adresse calculée |
| 1.2 | O(1) | Index négatif résolu en `len + i`, puis accès direct |
| 1.3 | O(n) | `in` sur list = recherche linéaire |
| 1.4 | O(1) | `in` sur set = hachage |
| 1.5 | O(1) | `in` sur dict = hachage des clés |
| 1.6 | O(n) | `count` parcourt toute la liste |
| 1.7 | O(n) | `pop(0)` décale tous les éléments |
| 1.8 | O(1) | Accès direct par index |
| 1.9 | O(1) | `dict.get` = hachage |
| 1.10 | O(n + m) | Construction des sets O(n+m) + intersection O(min(n,m)) |

## Exercice 2 — Prédictions

### 2.1 — `[1, 2, 3]`
`dict.keys()` retourne une vue sur les clés, en **ordre d'insertion**
(garanti depuis Python 3.7). `list()` matérialise cette vue.

### 2.2 — `3`
Un set élimine les doublons : `{3, 1, 2, 1, 3}` → `{1, 2, 3}`.

### 2.3 — `TypeError: unhashable type: 'list'`
Un tuple n'est hashable que si **tous ses éléments** sont hashables.
`(1, [2, 3])` contient une liste (mutable, non hashable).

### 2.4 — `TypeError: unhashable type: 'list'`
Les éléments d'un set doivent être hashables.

### 2.5 — `RuntimeError: dictionary changed size during iteration`
Modifier un dict pendant son itération est interdit.
**Correction** : `for k in list(d.keys()): ...`

## Exercice 6 — Design de la file de tâches

### 6.1 — Structures

| Opération | Structure | Complexité |
|-----------|-----------|:----------:|
| `enqueue` | `deque.append` | O(1) |
| `dequeue` | `deque.popleft` | O(1) |
| `contains` | `set` | O(1) moyen |
| `size` | `len(deque)` | O(1) |

### 6.2 — Alternative
`list.pop(0)` est O(n) : décale tous les éléments. `deque.popleft()`
est O(1) car implémenté en liste doublement chaînée de blocs.

### 6.3 — Contains avec tâches non hashables
Stocker les **identifiants** (hashables) dans le set, pas les objets
complets.

### 6.4 — FIFO à priorité égale
`heapq` + compteur d'insertion : `(priority, insertion_order, task)`.
Tuple comparable, ordre FIFO préservé pour même priorité.

### 6.5 — Compromis choisi
Mémoire (duplication liste + set) vs performance (O(1) partout).
Choix : performance, avec synchronisation soignée des deux structures.