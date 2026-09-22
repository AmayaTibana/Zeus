import math

def print_something():
    print("#########")
    print("using for a comment block")
    print("#########")

something = print_something();
print(something)
print(type(something))

def return_one_hundred():
    return 100

print(return_one_hundred())
print(return_one_hundred() * return_one_hundred())
print(return_one_hundred() * 5)

def calculate_average(numbers):
    return sum(numbers)/len(numbers)


print(calculate_average([10,20,30,40,]))


def calculate_average_2(numbers2):
    return sum(numbers2), len(numbers2), sum(numbers2)/len(numbers2)

print(calculate_average_2([10,20,30,40]))
