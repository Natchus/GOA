list = [10, 25, "cat", "hello", 3.14, 2.71, True, False]

integers = [x for x in list if type(x) == int]
strings = [x for x in list if type(x) == str]
floats = [x for x in list if type(x) == float]
booleans = [x for x in list if type(x) == bool]

print(integers)
print(strings)
print(floats)
print(booleans)