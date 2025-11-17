list = [10, 25, "cat", "hello", 3.14, 2.71, True, False]
integers=[]
strings=[]
floats=[]
booleans=[]
for a in list:
    if type(a)==int:
        integers.append(a)
    elif type(a)==str:
        strings.append(a)
    elif type(a)==float:
        floats.append(a)
    elif type(a)==bool:
        booleans.append(a)

print(integers)
print(strings)
print(floats)
print(booleans)
print(integers)
print(strings)
print(floats)
print(booleans)