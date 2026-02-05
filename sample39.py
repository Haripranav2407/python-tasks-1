n =int(input ("enter a num:"))
sum =0 
for i in range(1, n+1):
    sum+=i
    if sum==n :
        print("perfect number ")
        break
else :
    print("not a perfect number ")