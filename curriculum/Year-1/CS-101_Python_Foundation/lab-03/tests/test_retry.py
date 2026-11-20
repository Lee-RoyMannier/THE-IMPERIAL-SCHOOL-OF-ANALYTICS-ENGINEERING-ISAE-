
from lab import retry
import pytest

# TEST 1 : La fonction réussit dès le premier appel
def test_success_first_attempt():
    """
        Test une fonction avec 1 essaie réussi
    """
    attempts = 0

    @retry(max_attempts=3, exceptions=(Exception,))
    def fake_api():
        nonlocal attempts
        attempts += 1
        return "Success"

    result = fake_api()

    assert result == "Success"
    assert attempts == 1


# TEST 2 : La fonction échoue 2 fois puis réussit
def test_success_after_two_failures():
    """
    Test une fonction avec 2 echoie et 1 reussi

    """
    attempts = 0

    @retry(max_attempts=3, exceptions=(ConnectionError,))
    def fake_api():
        nonlocal attempts
        attempts += 1

        if attempts <= 2:
            raise ConnectionError("API unavailable")

        return "Success"

    result = fake_api()

    assert result == "Success"
    assert attempts == 3


# TEST 3 : La fonction échoue systématiquement
def test_all_attempts_fail():
    'test la fonction qui echoue toujours apres 3 tentatives'
    attempts = 0

    @retry(max_attempts=3, exceptions=(ConnectionError,))
    def fake_api():
        nonlocal attempts
        attempts += 1
        raise ConnectionError("API unavailable")

    with pytest.raises(ConnectionError, match="API unavailable"):
        fake_api()

    assert attempts == 3
