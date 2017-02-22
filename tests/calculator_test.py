import pytest
from calculator import Calc, SoBigException

def test_calc():
    calc = Calc()
    assert calc is not None

def test_calc_can_add():
    calc = Calc()
    assert calc.add(1, 2) == 3
    assert calc.add(2, 2) == 4

def test_calc_can_sub():
    calc = Calc()
    assert calc.sub(4, 3) == 1

def test_calc_mode_argument():
    calc = Calc()
    assert calc.mode == calc.MODE_NORMAL
    
    calc = Calc(mode=Calc.MODE_VERBOSE)
    assert calc.mode == calc.MODE_VERBOSE

def test_calc_verbose_mode_add():
    calc = Calc(mode=Calc.MODE_VERBOSE)
    assert calc.add('ONE', 'ONE') == 'TWO'
    assert calc.add('ONE', 'TWO') == 'THREE'
    assert calc.add('ONE', 'THREE') == 'FOUR'
    assert calc.add('FIVE', 'FIVE') == 'TEN'

def test_calc_raises_exception_if_num_so_big():
    calc = Calc(mode=Calc.MODE_VERBOSE)
    with pytest.raises(SoBigException):
        calc.add('FIVE', 'SIX')
