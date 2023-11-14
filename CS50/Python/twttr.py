twttr = input("Input: ")
for chars in twttr:
    if not chars.upper() in ['A','E','I','O','U']:
        print(chars, end="")