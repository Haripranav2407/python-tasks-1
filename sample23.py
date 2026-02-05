a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if b**2-(4*a*c)>0:
    print("real and distinct")
elif  b**2-(4*a*c)==0:
    print("real and equal")
elif  b**2-(4*a*c)<0:
    print("imaginary")