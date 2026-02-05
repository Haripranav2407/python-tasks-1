n=input("Enter the number:")
count_even=0
count_odd=0
for i in n :
    if int(i)%2==0 :
        count_even+=1
    else:
        count_odd+=1
print("Even:",count_even)
print("Odd:",count_odd)