n=input("Enter the number:")
sum=0
for i in n :
    sum+=int(i)**3
if sum==int(n) :
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")