months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

loop = 1
while loop == 1:
    try:
        date_unformated = input("Date: ")
        date_unformated = date_unformated.lstrip()
        date_unformated = date_unformated.rstrip()
        date = date_unformated.replace(" ","/")
        parts_date = date.split("/")

        day = parts_date[1]
        month = parts_date[0]

        if day in months:
            print()
            continue

        if month in months and "," not in day:
            print()
            continue

        day = day.replace(",","")
        year = parts_date[2]

        for part in parts_date:
            if len(part) > 0:
                if part in months:
                    for index in range(len(months)):
                        if part == months[index]:
                            month = index + 1

            if ( int(month) >=1 and int(month) <=12 ) and ( int(day) >= 1 and int(day) <= 31):
                print(f"{int(year):04}-{int(month):02}-{int(day):02}")
                loop = 0
                break
    except:
        print()
        pass
