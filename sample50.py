number=int(input ("enter a number :"))
n =int(input("number repeated:"))
count=0 
while number!=0:
    digit=number%10
    if digit==n:
        count+=1
    number//=10
print("the repetition of", n , "in the given number is :", count)