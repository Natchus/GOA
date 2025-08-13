list = [10, 25, "cat", "hello", 3.14, 2.71, True, False]
for a in list:
    if type(a) == str:
        string=a.upper()
        print(string[-3:])