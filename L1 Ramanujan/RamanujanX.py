print("Ramanujan")

c = 0
r = 0
a = 0
b = 2
solutions = []
counter = 0

n = int(input("n= "))
print()	
k = int(n**(1/3))

for i in range(1,k+1):
	a = ((n-(i**3))**(1/3)

	if a**3 == n-i**3 :
		solutions.append(a)


print(solutions)