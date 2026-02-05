a=int(input("a:"))
b=int(input("b:"))
if (a+b)>(a*b):
    print(f"{a+b} is greater")
elif (a+b)<(a*b):
    print(f"{a*b} is greater")
else:
    print("both are equal")