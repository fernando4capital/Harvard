def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    if len(s) == 6:
        if s[2].isalpha() == False or s[3].isalpha() == False:
            return False

    pointer = 0
    while pointer < len(s):
        if s[pointer].isalpha() == False:
            if s[pointer] == '0':
                return False
            else:
                break
        pointer += 1

    for c in s:
        if c in [' ','?','!','.',':','/']:
            return False

    return True

if __name__ == "__main__":
    main()