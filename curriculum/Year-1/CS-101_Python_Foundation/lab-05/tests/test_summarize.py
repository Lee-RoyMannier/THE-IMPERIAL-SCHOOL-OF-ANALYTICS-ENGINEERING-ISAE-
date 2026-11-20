from lab import Transaction, Summary, summarize

def test_nominal():
    transactions_lst = [
                    {"id": 1, "amount": 42.50, "category": "food",   "date": "2026-01-03"},
                    {"id": 2, "amount": 180.00, "category": "travel", "date": "2026-01-03"},
                    {"id": 3, "amount": 12.00, "category": "food",   "date": "2026-01-04"},
                    {"id": 4, "amount": 250.00, "category": "tech",   "date": "2026-01-04"},
                    {"id": 5, "amount": 75.00, "category": "food",   "date": "2026-01-05"},
    ]   

    transactions: list[Transaction] = [Transaction(id=t["id"], amount=t["amount"], category=t["category"], 
                                        transaction_date=t["date"]) for t in transactions_lst]

    summary = summarize(transactions)

    assert summary == Summary(total=559.5, by_category={'food': 129.5, 'travel': 180.0, 'tech': 250.0}, 
                                count=5, biggest=Transaction(id=4, amount=250.0, category='tech', transaction_date='2026-01-04'))

def test_first_max():
    transactions_lst = [
                    {"id": 1, "amount": 1242.50, "category": "food",   "date": "2026-01-03"},
                    {"id": 2, "amount": 180.00, "category": "travel", "date": "2026-01-03"},
                    {"id": 3, "amount": 12.00, "category": "food",   "date": "2026-01-04"},
                    {"id": 4, "amount": 250.00, "category": "tech",   "date": "2026-01-04"},
                    {"id": 5, "amount": 75.00, "category": "food",   "date": "2026-01-05"},
    ]   

    transactions: list[Transaction] = [Transaction(id=t["id"], amount=t["amount"], category=t["category"], 
                                        transaction_date=t["date"]) for t in transactions_lst]

    summary = summarize(transactions)
    assert summary == Summary(total=1759.5, by_category={'food': 1329.5, 'travel': 180.0, 'tech': 250.0}, count=5, 
                            biggest=Transaction(id=1, amount=1242.50, category='food', transaction_date="2026-01-03"))
