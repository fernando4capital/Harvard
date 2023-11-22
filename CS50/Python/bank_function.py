def main():
    getMoney = input("Greeting:")
    print(f"{value(getMoney)}")

def value(greeting):
    if "hello" in greeting.lower().strip():
        return 0
    elif "hello" not in greeting.lower().strip() and greeting.lower().rfind("h") == 0:
        return 20
    else:
        return 100

if __name__ == '__main__':
    main()