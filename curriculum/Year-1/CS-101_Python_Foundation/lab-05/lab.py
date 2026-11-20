from dataclasses import dataclass, field
import csv

@dataclass
class Transaction:
    id: int
    amount: float
    category: str
    transaction_date: str


@dataclass
class Summary:
    total: float = 0.0
    by_category: dict[str, float] = field(default_factory=dict)
    count: int = 0
    biggest: Transaction | None = None



def summarize(transactions: list[Transaction]) -> Summary:
    """Calcule les statistiques d'une liste de transactions.

    Returns:
        Summary: résumé contenant le total, les catégories,
                 le nombre de transactions et la plus grosse transaction.
    """
    summary = Summary()
    
    for transaction in transactions:
        amount = transaction.amount
        category = transaction.category

        summary.total += amount
        summary.count += 1

        summary.by_category[category] = (summary.by_category.get(category,0) + amount)

        if summary.biggest is None or amount > summary.biggest.amount:
            summary.biggest = transaction

    return summary


def load_transactions(path: str) -> list[Transaction]:
    """
        Fonction permettant de traiter un fichier csv de transaction et de retourner
        une liste d'objet Transaction

        Return
            Transaction objet
    """
    transactions = []

    with open(path) as f:
        data = csv.DictReader(f)
        for row in data:
            id_transaction = int(row.get("id"))
            amount_transaction = float(row.get("amount"))
            category = row.get("category")
            date_transaction = row.get("date")
            transaction = Transaction(id=id_transaction,amount=amount_transaction,category=category,transaction_date=date_transaction)
            transactions.append(transaction)

    return transactions


if __name__ == "__main__":
    path = "transactions.csv"
    all_transactions = load_transactions(path)
    print(all_transactions)