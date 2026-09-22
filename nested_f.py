# def countdown(n):
#     print(n)
#     if n ==  0:
#         return
#     else:
#         countdown(n -1)
# countdown(10)

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Sorry, must be an interger.")
    if number < 0:
        raise ValueError("Sorry, must be a number")
    def inner_factorial(number): #nested fuction calculation
        if number <= 1:
            return 1
        return number * inner_factorial(number-1)
    return inner_factorial(number)

print(factorial(4))