character=input("enter a character:")
if character.isdigit():
    print("digit")
elif character.isalpha():
    print("alphabet")
else:
    print("speacial character")