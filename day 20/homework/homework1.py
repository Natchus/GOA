name=input("enter your name:")
for a in name:
    if a.isupper():
        print(name.lower())
    else:
        print(name.upper())