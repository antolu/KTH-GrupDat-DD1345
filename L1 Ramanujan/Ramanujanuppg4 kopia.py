print("Ramanujan")
print()

c = 0
r = 0
a = 0
b = 2
counter = 0

n = int(input("n= "))
print()	

while a <= n**(1/3):

	a += 1
	b = int((n - (a-1)**3)**(1/3))

	while b > 0:
		c = a**3+b**3
		if c == n:
			counter += 1
			print(" a = ",a)
			print(" b = ",b)
			print()
		b -= 1 
		r += 1

	if counter == 2:						#Overflow check
		break
	r += 1

if counter == 2:
	print(" Antal iterationer: ",r)
else:
	print("Inga lösningar existerar! (probably)")
	print("Antal prövade kombinationer: ",r)