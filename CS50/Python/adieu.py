import inflect

p = inflect.engine()

array_names = []

while True:
    try:
        item_name = input("Name: ")
        array_names.append(item_name)

    except EOFError:
        print()
        break

list_of_names = p.join(array_names)
print (f"Adieu, adieu, to {list_of_names}")