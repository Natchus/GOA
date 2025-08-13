list = [10, 25, "cat", "hello", 3.14, 2.71, True, False]

integers = [a for a in list if type(a) == int]
strings = [a for a in list if type(a) == str]
floats = [a for a in list if type(a) == float]
booleans = [a for a in list if type(a) == bool]

print(integers)
print(strings)
print(floats)
print(booleans)