import random

def main():
    lvl = get_level()
    score = 0
    points = 0
    rounds = 1

    while rounds <= 10:
        x, y = generate_integer(lvl)
        points = play(x, y)
        score = score + points
        rounds +=1

    print(f"Score: {score}")

def play (x, y):
    z = int(x) + int(y)

    attempts = 0
    try:
        while attempts < 3:
            resp = int(input(f"{x} + {y} = "))
            if resp == z:
                return 1
            else:
                attempts +=1
                print("EEE")
    except:
        attempts +=1
        print("EEE")

    print(f"{x} + {y} = {x+y}")
    return 0

def get_level():
    while True:
        try:
            level = int(input("Level :"))
            if level > 0 and level < 4:
                return level
        except:
            continue


def generate_integer(level):

    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y

if __name__ == "__main__":
    main()