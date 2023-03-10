largest = None
smallest = None

a  = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
    	try:
    		a.append(int(num))
    	except:
    		print("Invalid Input")



b = []

for i in a:
	b.append(int(i))


for num in b:
	if largest is None:
		largest = num
	elif num > largest:
		largest = num

for num in b:
	if smallest is None:
		smallest = num
	elif num < smallest:
		smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)


