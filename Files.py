
years = []

fin = open('years.txt', 'r')
for line in fin:
    line = line.replace("\n", "")
    years.append(line)

print(years)
                        