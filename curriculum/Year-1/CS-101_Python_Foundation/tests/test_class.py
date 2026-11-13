from lab import ShoppingCart

"""Tests de ShoppingCart — indépendance des instances."""

from exercises import ShoppingCart


def test_carts_have_independent_items():
    """Deux paniers ne partagent pas leurs items.

    Ce test **échoue** avec la version buggée (attribut de classe
    partagé) et **passe** avec la version corrigée (`__init__`).
    """
    a = ShoppingCart()
    b = ShoppingCart()

    a.add("bread")
    b.add("milk")

    assert a.items == ["bread"]
    assert b.items == ["milk"]


def test_single_cart_add():
    """Un seul panier se comporte normalement."""
    cart = ShoppingCart()
    cart.add("apple")
    cart.add("bread")

    assert cart.items == ["apple", "bread"]


def test_new_cart_is_empty():
    """Un panier fraîchement créé est vide."""
    cart = ShoppingCart()
    assert cart.items == []


def test_many_carts_are_independent():
    """Test de robustesse sur un grand nombre d'instances."""
    carts = [ShoppingCart() for _ in range(10)]

    for i, cart in enumerate(carts):
        cart.add(f"item-{i}")

    for i, cart in enumerate(carts):
        assert cart.items == [f"item-{i}"]