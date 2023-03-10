s = open("mbox-short.txt")

l = []

for i in s:
    a = i.rstrip()
    b = a.split()
    if len(b) < 1:
        continue
    if b[0] == "From:":
        l.append(b[1])

d = {}

for val in l:
    if val not in d:
        d[val] = 1
    else:
        d[val] += 1

max = 0

for i in d:
    if d[i] > max:
        max = d[i]
        
        
for i in d:
    if max == d[i]:
        print(i,d[i])

