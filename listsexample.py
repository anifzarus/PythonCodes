fname = input("Enter file name: ")
a = open(fname)

b = []
for words in a:

    word = words.rstrip()
    if word.startswith('From:'):
        sec = word.split()
        b.append(sec)

count = 0

for i,j in b:
    print(j)
    count += 1

print("There were", count ,"lines in the file with From as the first word")
