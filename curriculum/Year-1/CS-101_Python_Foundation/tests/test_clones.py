"""Tests des fonctions shallow_clone et deep_clone."""

from lab import deep_clone, shallow_clone


# ─────────── shallow_clone ───────────

def test_shallow_clone_flat_list():
    """Une liste plate est copiée : nouvelle liste externe."""
    original = [1, 2, 3]
    clone = shallow_clone(original)

    assert clone == original
    assert clone is not original


def test_shallow_clone_shares_inner_lists():
    """Les sous-listes restent partagées par référence."""
    original = [[1, 2], [3, 4]]
    clone = shallow_clone(original)

    clone[0][0] = 99

    assert original[0][0] == 99  # partagé
    assert clone[0] is original[0]


# ─────────── deep_clone ───────────

def test_deep_clone_flat_list():
    """Une liste plate est copiée."""
    original = [1, 2, 3]
    clone = deep_clone(original)

    assert clone == original
    assert clone is not original


def test_deep_clone_independence_of_inner_lists():
    """Les sous-listes sont indépendantes après clonage."""
    original = [[1, 2], [3, 4]]
    clone = deep_clone(original)

    clone[0][0] = 99

    assert original[0][0] == 1     # original inchangé
    assert clone[0] is not original[0]


def test_deep_clone_arbitrary_depth():
    """Gère les listes imbriquées de profondeur arbitraire."""
    original = [1, [2, [3, [4, [5]]]]]
    clone = deep_clone(original)

    clone[1][1][1][1][0] = 999

    assert original[1][1][1][1][0] == 5


def test_deep_clone_empty_list():
    """Cas limite : liste vide."""
    assert deep_clone([]) == []