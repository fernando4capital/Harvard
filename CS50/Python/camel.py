def main():
    askCamel = input("camelCase:")
    snake = convert(askCamel)
    print (f"snake_case:",snake)

def convert(var_name):
    var_name_splits = [char for char in var_name]
    var_snake = ""

    for var_name_split in var_name_splits:
        if var_name_split.isupper():
            var_snake = var_snake + "_" + var_name_split.lower()
        else:
            var_snake = var_snake + var_name_split

    return (var_snake)

if __name__ == "__main__":
    main()
