from fuel import convert, gauge
import pytest

def main():
    test_correct_input()
    test_division_error()
    test_value_error()

def test_correct_input():
    assert convert('1/100') == 1 and gauge(0.01) == "E"
    assert convert('99/100') == 99 and gauge(99) == "F"
    assert convert('1/4') == 25 and gauge(25) == "25%"
    assert convert('1/100') == 1 and gauge(1) == "E"

def test_divison_error():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert('nada/bobagem')

if __name__ == '__main__':
    main()
