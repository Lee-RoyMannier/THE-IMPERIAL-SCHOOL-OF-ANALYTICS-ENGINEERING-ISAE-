**Objectif : reproduire les patterns sur un filtre différent.**

Avec les mêmes transactions :

1. List comprehension : toutes les transactions du 4 janvier (date == "2026-01-04").

2. Generator + sum : la somme totale des montants > 50 €.

3. Dict comprehension : le montant total par catégorie (pas le count, le total).

4. Format attendu : 3 snippets de 3-5 lignes, avec un print du résultat. Docstring inutile ici — c'est un exercice de syntaxe.

Règle : si vous utilisez une list comprehension à l'étape 2, vous perdez l'intérêt pédagogique. L'objectif est d'utiliser un générateur avec sum().

**Objectif : écrire une fonction qui traite un flux de transactions sans matérialiser.**
def summarize(transactions: list[dict]) -> dict:
    """Retourne un résumé agrégé des transactions.

    Returns:
        {
            "total": float,              # somme de tous les montants
            "by_category": dict[str, float],  # total par catégorie
            "count": int,                # nombre de transactions
            "biggest": dict | None,      # transaction au montant max
        }
    """

Contraintes :

Un seul passage sur transactions. Interdit : sum(...), puis max(...), puis len(...) — ça ferait 3 passages.

Utilisez une boucle for avec des accumulateurs, OU un générateur si pertinent. Mais un seul parcours.

Docstring + type hints.

2 tests pytest : cas nominal (5 transactions), cas vide ([] → {"total": 0, "by_category": {}, "count": 0, "biggest": None}).

Indice : un for unique avec mise à jour d'accumulateurs. Pas besoin de générateur ici — le générateur serait artificiel. L'objectif est de comprendre quand ne pas l'utiliser.