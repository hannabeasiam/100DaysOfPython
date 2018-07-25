"""
    Create a multiply two function given any input
    multiplier function can take an input and return a value several times that input
"""

"""
def mul_by_two(x):
    return x*2

print(mul_by_two(4))
print(mul_by_two(4.5))


# print(mul_by_two(4b))


def v2_mul_by_two(x):
    if isinstance(x, int):
        return x*2
    elif isinstance(x, float):
        return x*2
    else:
        print('Invalid input')

print(v2_mul_by_two(4))
print(v2_mul_by_two(4.5))
print(mul_by_two('hgf'))
print(mul_by_two('hgf'))

    SyntaxError: invalid syntax
"""

"""
    map(f, iterable) receive input as function f and iterable 



def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result


# result = two_times([1, 2, 3])
# result = two_times(1) -> TypeError: 'int' object is not iterable

print(result)



def two_times(x):
    return x*2

result = list(map(two_times, [3, 5, 3]))
print(result)



result = list(map(lambda a: a*2, [3, 5, 3]))
print(result)
"""


