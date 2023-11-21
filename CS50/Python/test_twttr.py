from twttr import shorten

def main():
    test()

def test():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'

def test_numbers():
    assert shorten('123') == '123'

def test_punctuation():
    assert shorten(".,?!") == ".,?!"

if __name__ == '__main__':
    main()