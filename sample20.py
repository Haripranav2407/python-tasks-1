cost_price=float(input("enter cp:"))
selling_price=float(input("enter sp:"))
if cost_price>selling_price:
    print("profit")
elif cost_price<selling_price:
    print("loss")
else:
    print("no profit no loss")