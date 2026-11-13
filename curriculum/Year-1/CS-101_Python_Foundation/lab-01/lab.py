
---

## 📄 `lab.py` 

```python
"""CS-101 — Lab 01 : Références, mutabilité, identité.

Implémentations corrigées des exercices 3, 4 et 5.
"""

from typing import Any, Optional, TypeVar

T = TypeVar("T")


# ─────────────────────────────────────────────────────────────
# Exercice 3 — safe_append
# ─────────────────────────────────────────────────────────────

def safe_append(x: T, l: Optional[list[T]] = None) -> list[T]:
    """Ajoute x à une liste existante ou crée une nouvelle liste.

    Cette fonction évite le piège classique du mutable par défaut
    (`def f(x, l=[])`) : la sentinelle est `None` (immuable) et une
    nouvelle liste est créée à chaque appel sans `l`.

    Args:
        x: Élément à ajouter.
        l: Liste existante (facultative). Si `None`, une nouvelle
            liste `[x]` est créée.

    Returns:
        La liste contenant `x`. Si `l` est fourni, c'est le **même
        objet** qui est retourné (mutation in-place).

    Complexity:
        Time:  O(1) amortized (append)
        Space: O(1) additional (mutation in-place ou nouvelle liste
               d'un élément)
    """
    if l is None:
        l = []
    l.append(x)
    return l


# ─────────────────────────────────────────────────────────────
# Exercice 4 — Clones sans le module copy
# ─────────────────────────────────────────────────────────────

def shallow_clone(lst: list[T]) -> list[T]:
    """Crée une copie superficielle d'une liste.

    Les éléments externes sont dupliqués ; les objets mutables
    internes (sous-listes, dicts, …) restent **partagés** par
    référence.

    Args:
        lst: La liste à copier.

    Returns:
        Une nouvelle liste externe contenant les mêmes références
        internes.

    Complexity:
        Time:  O(n), n = nombre d'éléments de la liste externe
        Space: O(n) pour la nouvelle liste
    """
    return lst[:]


def deep_clone(lst: list) -> list:
    """Crée une copie profonde récursive d'une liste imbriquée.

    Gère les listes imbriquées de profondeur arbitraire. Ne clone
    pas les tuples, dicts ou sets imbriqués (limite documentée :
    pour un usage général, préférer `copy.deepcopy`).

    Args:
        lst: La liste à cloner.

    Returns:
        Une nouvelle structure de listes entièrement indépendante.

    Complexity:
        Time:  O(N), N = nombre total d'éléments à tous les niveaux
        Space: O(N) pour la structure clonée
    """
    new_lst: list = []
    for element in lst:
        if isinstance(element, list):
            new_lst.append(deep_clone(element))
        else:
            new_lst.append(element)
    return new_lst


# ─────────────────────────────────────────────────────────────
# Exercice 5 — ShoppingCart 
# ─────────────────────────────────────────────────────────────

class ShoppingCart:
    """Panier d'achat avec items propres à chaque instance.

    Correction du bug de l'attribut de classe partagé : `items`
    est défini dans `__init__`, donc chaque instance possède sa
    propre liste.
    """

    def __init__(self) -> None:
        """Initialise un panier vide."""
        self.items: list[str] = []

    def add(self, item: str) -> None:
        """Ajoute un item au panier.

        Args:
            item: Le nom de l'article à ajouter.
        """
        self.items.append(item)