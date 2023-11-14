due_amount = 50
while due_amount > 0:
    print(f"Amount Due:", due_amount)
    inserted_coin = int(input("Insert Coin:"))
    if inserted_coin in [5,10,25]:
        due_amount -= inserted_coin

pay_change = abs(due_amount)
print(f"Change Owed:",pay_change)