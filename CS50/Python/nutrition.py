fruits_dict = {
    "apple": 130,
    "avocado": 50,
    "sweet cherries":100,
    "kiwifruit":90,
    "pear":100

    ## Any other item (fruit) that you need to test must be included in the fruits_dict dictionary
}

item = input("Item:").lower()

for key in fruits_dict:
    if key == item:
        print("Calories:", fruits_dict[key])