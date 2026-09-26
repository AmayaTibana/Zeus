import sys

fname = input("Enter a file name: ")
try:
    fhand = open(fname)

except:
    print("File cannot be opened: ", fname)
    sys.exit()
count = 0
for line in fhand:
    count = count +1
print('there were', count, 'lines in', fname)