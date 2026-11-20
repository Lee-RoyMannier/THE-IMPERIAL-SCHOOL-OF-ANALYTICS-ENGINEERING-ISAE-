from lab import load_transactions

def test_load_transactions(tmp_path):
    # 1. Créer un fichier temporaire
    csv_file = tmp_path / "transactions.csv"
    csv_file.write_text(
        "id,amount,category,date\n"
        "1,42.50,food,2026-01-03\n"
        "2,180.00,travel,2026-01-03\n"
    )

    # 2. Tester la fonction
    transactions = load_transactions(str(csv_file))

    # 3. Vérifier le résultat
    assert len(transactions) == 2
    assert transactions[0].amount == 42.50
    assert transactions[0].category == "food"

def test_load_empty_transactions(tmp_path):
    # 1. Créer un fichier temporaire
    csv_file = tmp_path / "transactions.csv"
    csv_file.write_text(
        "id,amount,category,date\n"
    )

    # 2. Tester la fonction
    transactions = load_transactions(str(csv_file))

    # 3. Vérifier le résultat
    assert len(transactions) == 0
    assert transactions == []