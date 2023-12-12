import re

def main():
    read_ipaddress()

def read_ipaddress():
    is_ipvalid = validate(input("IPv4 Address:"))
    print(is_ipvalid)

def validate(ipaddress):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ipaddress):
        numb3rs_list = ipaddress.split(".")
        for numb3r in numb3rs_list:

            int_number = int(numb3r)

            if int_number < 0 or int_number > 255:
                return False
        return True

    else:
        return False

if __name__ == "__main__":
    main()