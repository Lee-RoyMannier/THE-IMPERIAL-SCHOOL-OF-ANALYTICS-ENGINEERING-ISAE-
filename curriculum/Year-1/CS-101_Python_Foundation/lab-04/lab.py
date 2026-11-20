


transactions = [
    {"id": 1, "amount": 42.50, "category": "food",   "date": "2026-01-03"},
    {"id": 2, "amount": 180.00, "category": "travel", "date": "2026-01-03"},
    {"id": 3, "amount": 12.00, "category": "food",   "date": "2026-01-04"},
    {"id": 4, "amount": 250.00, "category": "tech",   "date": "2026-01-04"},
    {"id": 5, "amount": 75.00, "category": "food",   "date": "2026-01-05"},
]

# Exercice
## List comprehension : toutes les transactions du 4 janvier (date == "2026-01-04").
## Generator + sum : la somme totale des montants > 50 €.
## Dict comprehension : le montant total par catégorie (pas le count, le total).
a = [t for t in transactions if t["date"]=="2026-01-04"]
b = sum(t["amount"] for t in transactions if t["amount"] > 50)
c = {cat: sum(t["amount"] for t in transactions if t["category"] == cat) for cat in {t["category"] for t in transactions} }

print(a)
print(b)
print(c)

#####################
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
    total = 0
    c = 0
    by_category = {}

    if len(transactions) == 0:
        return {"total": total,             
                "by_category": by_category, 
                "count": c,              
                "biggest": None
        }

    max_amount = transactions[0]["amount"]
    biggest =  transactions[0]
    for t in transactions:
        total += t["amount"]
        c += 1

        if t["amount"] > max_amount:
            biggest = t
            max_amount = t["amount"]
        
        by_category[t["category"]] = by_category.get(t["category"],0) + t["amount"]
    
    return {"total":total,"by_category": by_category, "count":c,"biggest":biggest}

print(summarize(transactions))
