def main():
    fraction = input("Fraction: ")
    convert_fraction = convert(fraction)
    gauge_result = gauge(convert_fraction)
    print (gauge_result)

def convert(fraction):
    while True:
        try:
            num, den = fraction.split("/")
            numerator = int(num)
            denominator = int(den)
            fuel = numerator / denominator

            if fuel <=1:
                percent_fuel = int(fuel * 100)
                return percent_fuel
            else:
                pass

        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):

    print (f"percentage: {percentage}")

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)+"%"

if __name__ == "__main__":
    main()