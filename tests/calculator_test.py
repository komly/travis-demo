from calculator import Calc

def test_calc():
    calc = Calc()
    assert calc is not None

def test_calc_can_add():
    calc = Calc()
    assert calc.add(1, 2) == 3
    assert calc.add(2, 2) == 4
