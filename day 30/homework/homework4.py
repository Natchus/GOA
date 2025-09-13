number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
odd = set()
for i in number:
    if i % 2 != 0:
        odd.add(i)
print(list(odd))