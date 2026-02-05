units=int(input("number of units:"))
bill=0
if units<=100:
    bill=units
elif(units<=200):
    bill=(units-100)*2+100
elif(units<=300):
    bill=(units-200)*3+200
elif(units>300):
    bill=(units-300)*5+300
print("Total Bill:",bill)