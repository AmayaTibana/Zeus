fname = input("enter a name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened: ", fname)
    exit()

count = 0
for line in fhand:
    count = count + 1
print('there were', count, 'lines in', fname)