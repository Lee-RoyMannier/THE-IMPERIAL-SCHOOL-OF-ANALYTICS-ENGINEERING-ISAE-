from lab import paginate
from itertools import count, islice

def test_nominal():
    """
        test de base pour récupérerer une list avec 3 element par page
    """
    numbers = list(islice(count(),7))
    page_size = 3

    result = list(paginate(numbers,page_size))
    assert result == [[0,1,2], [3,4,5], [6]]



def test_divisible():
    """
        test de divisiblité de list 6 element avec 3 par pages
    """
    numbers = list(islice(count(),6))
    page_size = 3

    result = list(paginate(numbers,page_size))
    assert result == [[0,1,2], [3,4,5]]


def test_empty_list():
    """Vérifie qu'une liste vide ne produit aucune page."""
    
    numbers = list()
    page_size = 3

    result = list(paginate(numbers,page_size))
    assert result == []


def test_infinite_iterable():
    """ test avec un iterable infini """
    numbers = count()

    result = list(islice(paginate(numbers, 3), 3))

    assert result == [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]