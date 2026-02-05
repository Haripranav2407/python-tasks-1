marks=int(input("enter marks:"))
if(marks<=100):
    if(marks>=90):
        print("A+")
    elif(marks>=80):
        print("A")
    elif(marks>=70):
        print("B")
    elif(marks>=60):
        print("C")
    elif(marks>=35):
        print("d")
    else:
        print("Fail")
else:
    print("invalid")