while True:
    fraction = input("Fraction: ")
    try:
        num, den = fraction.split("/")
        numerator = int(num)
        denominator = int(den)

        percentage_fuel = numerator / denominator

        if numerator > denominator:
            continue
        else:
            break

        if percentage_fuel <=1:
            break

    except (ValueError, ZeroDivisionError):
        continue

tank = round(percentage_fuel * 100)

if tank <= 1:
   print ("E")
elif tank >= 99:
   print ("F")
else:
   print(f"{tank}%")