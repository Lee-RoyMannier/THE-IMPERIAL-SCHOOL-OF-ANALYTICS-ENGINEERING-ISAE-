from lab import summarize

def test_transaction():
    transactions = [
    {"id": 1, "amount": 42.50, "category": "food",   "date": "2026-01-03"},
    {"id": 2, "amount": 180.00, "category": "travel", "date": "2026-01-03"},
    {"id": 3, "amount": 12.00, "category": "food",   "date": "2026-01-04"},
    {"id": 4, "amount": 250.00, "category": "tech",   "date": "2026-01-04"},
    {"id": 5, "amount": 75.00, "category": "food",   "date": "2026-01-05"},
    ]

    result = summarize(transactions)

    assert result == {'total': 559.5, 'by_category': {'food': 129.5, 'travel': 180.0, 'tech': 250.0}, 'count': 5, 'biggest': {'id': 4, 'amount': 250.0, 'category': 'tech', 'date': '2026-01-04'}}

def test_empty_lst():
    transactions = []
    result = summarize(transactions)

    assert result == {"total": 0, "by_category": {}, "count": 0, "biggest": None}