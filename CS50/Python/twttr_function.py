def main():
    twttr = input('Input: ')
    print(shorten(twttr))

def shorten(word):
    key_vowels = ['A', 'E', 'I', 'O', 'U']

    for vowel in key_vowels:
        word = word.replace(vowel, '')
        word = word.replace(vowel.lower(), '')
    return word

if __name__ == '__main__':
    main()