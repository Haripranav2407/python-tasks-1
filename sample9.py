n=int(input("enter number:"))
if n<=9:
    print(n)
elif n>=10:
    last_digit=n%10
    print(last_digit)