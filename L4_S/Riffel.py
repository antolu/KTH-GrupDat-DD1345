nkort = int(input("Antalet kort i kortleken: "))

kortlek = []
riffel = []
counter = 0

for i in range(nkort):
	kortlek.append(i+1)

riffel2 = kortlek

while riffel != kortlek:
	riffel = []
	for i in range(int(nkort/2)):
		riffel.append(riffel2[i])
		riffel.append(riffel2[i+int(nkort/2)])
	riffel2 = riffel


	counter += 1

print("Antalet kuperingar: ", counter)