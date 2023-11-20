import random

while True:
    try:
        lvl_rdn_num = int(input("Level :"))
        if lvl_rdn_num > 0:
            break
    except:
        continue

rnd_num = random.randint(1, lvl_rdn_num)

while True:
    try:
        guess_num = int(input("Guess:"))
        if guess_num > 0:
            if guess_num < rnd_num:
                print("Too small!")
                continue

            if guess_num > rnd_num:
                print("Too large!")
                continue

            else:
                print("Just right!")
                break
    except:
        pass