import re

name = input("Enter file:")
if len(name) < 1:
    name = "week1.txt"

handle = open(name)

mylist = []
for line in handle:
    y = re.findall('[0-9]+', line)
    if len(y) != 0:
        for dig in y:
            mylist.append(int(dig))

print(sum(mylist))
