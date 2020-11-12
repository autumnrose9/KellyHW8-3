import sys

f3 = open("output.txt", "w")
f1 = open(sys.argv[1])
f2 = open(sys.argv[2])

flines1 = f1.readlines()
flines2 = f2.readlines()

in1 = flines1[0]
in2 = flines2[0]

list1 = in1.split(" ")
list2 = in2.split(" ")

list1Length = len(list1)
list2Length = len(list2)

out = []

if(list1Length > list2Length):
	count = list1Length
else:
	count = list2Length

while (count > 0):
	if(list1 != []):
		x1 = list1[-1].strip()
		out.append(x1)
		del list1[list1Length-1]
	if(list2 != []):
		x2 = list2[-1].strip()
		out.append(x2)
		del list2[list2Length-1]
	list1Length = len(list1)
	list2Length = len(list2)
	count -= 1

f1.close()
f2.close()

for l in out:
	f3.write(l)
	f3.write(' ')
f3.write('----------------------------------------')
f3.write('\n')
f3.close()
