# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
z = 0
count =0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line.find(":")
    y= float(line[x+1:])
    count +=1
    z +=y

print("Average spam confidence:", z/count)


counts = dict()
names = ['cse']
for name in names:
    counts[name] = counts.get(name, 0) + 1


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

mydict = dict()

for line in handle:
    if not line.startswith("From:"):
        continue
    email = line.split()[1]
    mydict[email] = mydict.get(email,0) + 1

largest = None
theone = None

for k, v in mydict.items():
	if (theone is None) or (v > largest):
        largest = v
        theone = k
print(k,v)
