d=int(input("Total Days:"))
y=d//365
w=d//7-(y*52)
rd=d%7
print(f"{y} years {w} weeks {rd} remaining days")