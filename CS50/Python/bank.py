getMoney = input("Greeting:")
if "how" in getMoney.lower().strip():
    print ("$20")
elif "what" in getMoney.lower().strip():
    print ("$100")
else:
    print ("$0")
