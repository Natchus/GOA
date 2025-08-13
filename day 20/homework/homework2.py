animals = ["Teddy", "johnny", "sky", "Paw"]
for a in animals:
    if a.istitle() and a[4:] == "":
        print(a[0:3])
    else:
        print("this name is too long")