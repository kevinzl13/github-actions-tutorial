from main import Calculadora


def test_sum():
    assert Calculadora().sum(2, 3) == 5
