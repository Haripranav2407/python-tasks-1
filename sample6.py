shape=input("Rectangle or Circle:")
if(shape=="Rectangle"):
    length=int(input("l:"))
    breadth=int(input("b:"))
    area=length*breadth
    perimeter=2*(length+breadth)
    print(f"area of rectangle:{area} and perimeter of rectangle:{perimeter}")
elif(shape=="circle"):
    radius=int(input("r:"))
    area=3.14*(radius**2)
    circumference=2*3.14*radius
    print(f"area of circle:{area} and circumference of circle{circumference}")
