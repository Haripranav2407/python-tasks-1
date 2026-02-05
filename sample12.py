a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if c>b and c>a:
    print(c," is largest")
elif b>c and b>a:
    print(b," is largest")
else:
    print(a," is largest")