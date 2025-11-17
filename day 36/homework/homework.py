def solution(string):
    return string[::-1]

def findSmallestInt(arr):
    return min(arr)

def greet():
    return("hello world!")

def summation(num):
    return sum(range(1, num + 1))

def double_integer(i):
    return i*2

def boolean_to_string(b):
    return(str(b))

def greet(name):
    return "Hello, " + name + " how are you doing today?"

def basic_op(operator, value1, value2):
    if operator is "+":
        return value1 + value2
    if operator is "-":
        return value1 - value2
    if operator is "*":
        return value1 * value2
    if operator is "/":
        return value1 / value2
    
def sum_array(a):
    if not a:
        return 0
    else:
        return sum(a)
    
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n*m