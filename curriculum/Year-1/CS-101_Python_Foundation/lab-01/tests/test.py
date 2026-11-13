from lab import safe_append

"""Tests de la fonction safe_append."""

from exercises import safe_append


def test_creates_new_list_when_none():
    """Sans argument l, une nouvelle liste [x] est créée."""
    result = safe_append(10)
    assert result == [10]


def test_no_shared_state_between_calls():
    """Deux appels successifs sans l ne partagent pas d'état."""
    a = safe_append(10)
    b = safe_append(20)

    assert a == [10]
    assert b == [20]
    assert a is not b


def test_mutates_provided_list_in_place():
    """Avec un argument l, la fonction mute l'objet fourni."""
    original = [1, 2, 3]
    result = safe_append(42, original)

    assert result == [1, 2, 3, 42]
    assert result is original  # même objet — mutation in-place


def test_works_with_empty_list():
    """Cas limite : liste vide fournie."""
    original = []
    result = safe_append(1, original)

    assert result == [1]
    assert result is original