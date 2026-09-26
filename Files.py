fname = input("enter a name")
fhand = open(fname)
count = 0
for line in fhand:
    count = count + 1
print('there were', count, 'lines in', fname)