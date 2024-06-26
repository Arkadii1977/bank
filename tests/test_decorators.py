import pytest

from src.decorators import log


def test_log():
    @log()
    def add(a, b):
        return a + b

    result = add(3, 3)
    assert result == 6


def test_log_second():
    @log
    def addd(a, b):
        return a + b
    with pytest.raises(Exception):
        addd(3, "3")
