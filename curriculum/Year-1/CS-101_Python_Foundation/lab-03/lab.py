# Exercice 4
import functools
from time import perf_counter, sleep

def timed(func):
    """Mesure et affiche le temps d'exécution d'une fonction."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Exécute la fonction et affiche sa durée d'exécution."""

        start = perf_counter()
        try:
            result = func(*args, **kwargs)
        finally:
            duration = perf_counter() - start
            print(
                    f"{func.__name__}: "
                    f"{duration * 1000:.2f} ms"
                )
        return result
    return wrapper


@timed
def calculate():
    """ Somme d'une liste"""
    return sum(range(1_000_000))


# Exerice 5
def retry(max_attempts,exceptions):
    if max_attempts <= 0:
        raise ValueError("max_attemps <= 0") 

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            
            for attemp in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except exceptions:
                    if attemp < max_attempts - 1:
                        sleep(0.1*(2**attemp))
                    else:
                        raise

        return wrapper
    return decorator

@retry(max_attempts=3, exceptions=(ZeroDivisionError,))
def dividedbyzero():
    t = [2,2,2]
    a = 0

    for i in t:
        a += (24//i)

    return a


# EXercice 6

def paginate(iterable, page_size):
    """
        Générateur qui yield des pages (iterable) de taille (page_size)
    """
    pages = []
    if page_size <= 0:
        raise ValueError("Page size inferieur ou égale a 0")

    for item in iterable:
        pages.append(item)

        if len(pages) == page_size:
            yield pages
            pages = []
    if pages:
        yield pages


