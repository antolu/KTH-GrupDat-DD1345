import random
import time

print("Ramanujan")
print()

counter = 0
c = 0
r = 0
c1 = 0
c2 = 0
a2 = 0
b2 = 0
n = int(input("n= "))					#Import number
maxnummer = int((n-1)**(1/3)+1)			#Maximum value for either variable

while True:
	if c1 != n:
		a1 = random.randint(0,maxnummer)		#Randomize variable a1
		b1 = random.randint(0,maxnummer)		#Randomize variable b2
		
		c1 = a1**3+b1**3
		if c1 == n:
			counter += 1
		
	if c2 != n:
		a2 = random.randint(0,maxnummer)		#Randomize variable a1
		b2 = random.randint(0,maxnummer)		#Randomize variable b2

		c2 = a2**3+b2**3
		if c2 == n and a1 != a2 != b1 != b2:
			counter+=1

	r += 1

	if r >= 100000 or counter == 2:				#Overflow check
		break

if counter == 2:
	print(" a1 = ", a1)
	print(" b1 = ", b1)
	print()
	print(" a2 = ", a2)
	print(" b2 = ", b2)
	print()
	print(" Number of tries: ", r)
else:
	print()
	print("Program failed")
	print("Solution probably doesn't exist")

