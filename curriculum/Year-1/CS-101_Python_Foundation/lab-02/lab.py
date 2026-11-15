"""CS-101 — Lab 02 : Structures de données fondamentales.

Implémentations corrigées des exercices 3, 4 et 5.
"""

from typing import Any, Optional, TypeVar

T = TypeVar("T")


# ─────────────────────────────────────────────────────────────
# Exercice 3 — deduplicate
# ─────────────────────────────────────────────────────────────

def deduplicate(lst: list[T]) -> list[T]:
    """Déduplique une liste en préservant l'ordre d'apparition.

    Un `set` seul ne suffit pas : il garantit l'unicité mais **pas
    l'ordre** d'itération (contrairement à `dict` depuis Python 3.7).
    On combine donc un `set` pour le test d'appartenance O(1) et une
    `list` pour conserver l'ordre d'apparition.

    Args:
        lst: La liste à dédupliquer.

    Returns:
        Une nouvelle liste sans doublons, dans l'ordre d'apparition
        des premiers éléments.

    Complexity:
        Time:  O(n) — n itérations, chacune O(1) amortized
        Space: O(n) — set + liste auxiliaire
    """
    uniques_values: set[T] = set()
    deduplicate_list: list[T] = []

    for element in lst:
        if element not in uniques_values:
            deduplicate_list.append(element)
            uniques_values.add(element)

    return deduplicate_list


# ─────────────────────────────────────────────────────────────
# Exercice 4 — two_sum
# ─────────────────────────────────────────────────────────────

def two_sum(lst: list[int], target: int) -> Optional[tuple[int, int]]:
    """Retourne les indices de deux éléments dont la somme vaut target.

    Approche : un seul passage. Pour chaque élément, on cherche son
    complément `target - num` dans un dict des valeurs déjà vues.
    Lookup O(1) moyen → complexité globale O(n).

    Une approche naïve (double boucle) serait O(n²) : n × n paires
    à examiner.

    Si plusieurs paires valides existent, retourne la **première**
    paire trouvée en ordre d'itération.

    Args:
        lst: La liste d'entiers.
        target: La somme cible.

    Returns:
        Un tuple `(i, j)` avec `i < j` et `lst[i] + lst[j] == target`,
        ou `None` si aucune paire n'existe.

    Complexity:
        Time:  O(n) — un seul passage, lookups O(1) dans le dict
        Space: O(n) — le dict stocke au plus n entrées
    """
    elements: dict[int, int] = {}

    for idx, num in enumerate(lst):
        complement = target - num
        if complement in elements:
            return (elements[complement], idx)
        elements[num] = idx

    return None


# ─────────────────────────────────────────────────────────────
# Exercice 5 — UserIndex
# ─────────────────────────────────────────────────────────────

class UserIndex:
    """Version naïve : liste, recherche linéaire O(n)."""

    def __init__(self) -> None:
        self.users: list[dict[str, Any]] = []

    def add(self, user_id: int, name: str) -> None:
        self.users.append({"id": user_id, "name": name})

    def get(self, user_id: int) -> Optional[dict[str, Any]]:
        """Complexity: Time O(n), Space O(1)."""
        for u in self.users:
            if u["id"] == user_id:
                return u
        return None


class UserIndexModified:
    """Version optimisée : dict, recherche O(1) moyen.

    Compromis :
    - Mémoire : le dict sur-alloue (load factor ~2/3) → plus de mémoire.
    - Ordre : garanti (Python ≥ 3.7), mais sémantiquement différent de
      la liste (une mise à jour d'ID écrase au lieu d'ajouter).
    - Recherche : O(1) moyen au lieu de O(n).
    """

    def __init__(self) -> None:
        self.users: dict[int, dict[str, Any]] = {}

    def add(self, user_id: int, name: str) -> None:
        self.users[user_id] = {"id": user_id, "name": name}

    def get(self, user_id: int) -> Optional[dict[str, Any]]:
        """Complexity: Time O(1) average, Space O(1)."""
        return self.users.get(user_id)