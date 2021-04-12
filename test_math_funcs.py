import math_funcs


def test_add():
    assert math_funcs.add(7, 3) == 10
    assert math_funcs.add(7) == 9


def test_product():
    assert math_funcs.product(7, 3) == 21
