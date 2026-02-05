angle1=int(input("enter angle1:"))
angle2=int(input("enter angle2:"))
angle3=int(input("enter angle3:"))
if angle1>0 and angle2>0 and angle3>0:
    if angle1+angle2+angle3<=180:
        print("valid")
    else:
        print("invalid")
else:
    print("incorrect")