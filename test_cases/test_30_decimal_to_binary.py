import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary


def test_decimal_10():
    assert decimal_to_binary(10) == "1010"


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_decimal_1():
    assert decimal_to_binary(1) == "1"


def test_decimal_8():
    assert decimal_to_binary(8) == "1000"


def test_decimal_15():
    assert decimal_to_binary(15) == "1111"


def test_negative_number_raises_error():
    with pytest.raises(ValueError):
        decimal_to_binary(-10)