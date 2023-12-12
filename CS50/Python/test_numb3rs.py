from numb3rs import validate

def main():
    test_ipaddress_format()
    test_ipaddress_range()

def test_ipaddress_format():
    assert validate(r'127.0.0.1') == True
    assert validate(r'127.0.0') == False
    assert validate(r'127.0') == False
    assert validate(r'127') == False

def test_ipaddress_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'1.512.512.512') == False
    assert validate(r'1.2.3.1000') == False

if __name__ == '__main__':
    main()