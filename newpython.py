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
