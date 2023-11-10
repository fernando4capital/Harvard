def main():
    askHour = input("What time is it?")
    now = convert(askHour)
    if now >= 7 and now <= 8:
        print ("breakfast time")
    elif now >= 12 and now <= 13:
        print ("lunch time")
    elif now >= 18 and now <= 19:
        print ("dinner time")
    else:
        print (now)

def convert(time):
    if ":" in time:
        hour,minutes = time.split(":")
        minuterToHours = int(minutes) / 60
        now = int(hour) + minuterToHours
        return (now)

if __name__ == "__main__":
    main()
