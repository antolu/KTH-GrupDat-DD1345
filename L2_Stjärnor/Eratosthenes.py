import time

n = int(input("Max primtal: "))
primtal = []
p = 2
x = 2

start = time.time()						#Starta tidtagning

for i in range(n):						#Stoppa in n stycken ettor i listan
	primtal.append(1)

while p <= n**0.5:						#Största primtalet är roten ur n
	if primtal[p-1] == 1:
		while x*p != 0  and x*p < n:		#Medan multipeln är nollskilld och mindre än n
			primtal[x*p-1] = 0				#Alla multiplar av talet p stryks ur listan
			x += 1							#Kolla alla multiplar
	x = 2
	p += 1								#Kolla nästa tal

prim = []

if n <= 10000:
	for i in range(len(primtal)):
		if primtal[i-1] == 1:
			prim.append(i)

#print(prim)
print()

end = time.time()
print(end-start,"sekunder")