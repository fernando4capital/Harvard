from bank import value

def main():
    test_value()

def test_value():
    assert value('hello') == 0
    assert value('Hell no') == 20
    assert value('welcome') == 100

if __name__ == '__main__':
    main()