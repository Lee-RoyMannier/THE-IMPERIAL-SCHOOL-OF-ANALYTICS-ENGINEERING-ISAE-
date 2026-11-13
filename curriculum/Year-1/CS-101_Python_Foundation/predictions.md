# CS-101 — Lab 01 — Prédictions (Ex 1 & 2)

## Exercice 1 — Prédictions de sortie

### 1.1 — `[1, 2, 3, 4] [1, 2, 3, 4]`

`b = a` ne copie pas l'objet : il lie `b` au **même objet liste** que `a`.
`b.append(4)` mute l'objet partagé. Les deux noms voient la mutation.

### 1.2 — `(1, 2, 3) (1, 2, 3, 4)`

Les tuples sont **immuables**. `b += (4,)` ne mute pas l'objet — il crée un
**nouvel objet tuple** `(1, 2, 3, 4)` et relie `b` dessus. `a` reste lié à
l'ancien tuple `(1, 2, 3)`.

### 1.3 — `[1, 2] [1, 2, 3]`

`b = b + [3]` est une **réassignation**, pas une mutation. L'expression
`b + [3]` crée une nouvelle liste ; `b` est ensuite relié à cette nouvelle
liste. `a` reste sur l'ancienne.

### 1.4 — `{'x': 1}` puis `{'x': 1}`

- `mutate(data)` : `d["x"] = 1` **mute** le dict partagé. `data` voit le
  changement.
- `reassign(data)` : `d = {"x": 1}` ne fait que **réassigner la liaison
  locale** `d` dans la fonction. L'objet `data` de l'appelant n'est pas
  affecté — il contenait déjà `{"x": 1}` depuis `mutate`, donc l'output
  est le même par coïncidence. Si `mutate` n'avait pas été appelé, le
  second `print` aurait affiché `{}`.

### 1.5 — `[1, 2, 3] [1, 2, 3, 4]`

`a[:]` crée une **copie superficielle** : `b` est une nouvelle liste
externe. `b.append(4)` mute cette nouvelle liste. `a` reste inchangé.

---

## Exercice 2 — `is` vs `==`

| # | Résultat | Justification |
|:-:|:--------:|---------------|
| 2.1 | `True` | Deux listes distinctes mais de même valeur. `==` compare les valeurs. |
| 2.2 | `False` | Deux littéraux distincts créent deux objets distincts. `is` teste l'identité. |
| 2.3 | `True` | `y = x` lie `y` au même objet. Même identité. |
| 2.4 | `True` | Deux littéraux `"abc"` ont la même valeur. `==` compare les valeurs. |
| 2.5 | `True` (en CPython) | **Détail d'implémentation** : CPython interne les chaînes littérales courtes. **Ne jamais utiliser `is` pour comparer des chaînes** dans du code professionnel. Utiliser `==`. |
| 2.6 | `True` | `None` est un singleton : un seul objet `None` existe. `==` fonctionne aussi. |
| 2.7 | `True` | `is None` est l'idiome correct et rapide pour tester `None`. À préférer à `== None`. |

**Règle professionnelle :** `is` est réservé à `None`, `True`, `False` et aux
singletons. Pour toute comparaison de valeur, utiliser `==`.