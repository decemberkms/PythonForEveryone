name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

mydict = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    tm = line.rstrip().split()[5]
    hr = tm.split(":")[0]
    mydict[hr] = mydict.get(hr, 0) + 1

tmp = list()

for k,v in mydict.items():
	tmp.append((k,v))

tmp.sort()
print(tmp)
