from lab import calculate, timed
import pytest

def test_good_return_value():
    result = calculate()

    assert result == 499999500000

def test_check_wraps():
    assert calculate.__name__ == "calculate"


def test_exception_is_propagated_and_time_is_printed(capsys):
    @timed
    def explode():
        raise ValueError("Something went wrong")

    with pytest.raises(ValueError, match="Something went wrong"):
        explode()

    captured = capsys.readouterr()

    assert "explode:" in captured.out
    assert "ms" in captured.out