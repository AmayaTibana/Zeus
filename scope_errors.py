total = 0

def sum(arg1, arg2):
    total = arg1 + arg2
    print("Local total:", total)
    return total
sum(10,20)
print("Global total:", total)