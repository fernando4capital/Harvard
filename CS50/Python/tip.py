def main():
    dollars_str = input("How much was the meal? ")
    dollars = dollars_to_float(dollars_str.replace('$', '').replace(',', ''))

    percent_str = input("What percentage would you like to tip? ")
    percent = percent_to_float(percent_str.replace('%',''))

    tip = dollars * (percent / 100)

    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d)

def percent_to_float(p):
    return float(p)

main()
