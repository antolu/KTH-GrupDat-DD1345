import random
import time

print("Ramanujan")
print()

c = 0
r = 0
n = int(input("n= "))					#Import number
maxnummer = int((n-1)**(1/3))			#Maximum value for either variable

while c != n:
	a = random.randint(0,maxnummer)		#Randomize variable a
	b = random.randint(0,maxnummer)		#Randomize variable b

	c = a**3+b**3						#Calculation

	r += 1

	if r >= 1000:						#Overflow check
		break

if c == n:
	print(" a = ", a)
	print(" b = ", b)
	print()
	print(" Number of tries: ", r)
else:
	print()
	print("Program failed")
	print("Solution probably doesn't exist")
	print()


