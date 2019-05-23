def triangelBasNer(a,b):
		while a >= 1:
			print(b*" " + a*"*")
			b +=1
			a -= 2

def triangelBasUpp(a,b):
	n=1
	while n <= a:
		print(int(b+(a-1)/2)*" " + n*"*")
		b -=1
		n += 2

triangelBasNer(9,10) #Bredd och indentering
print()
print()
print()
triangelBasUpp(9,10) #Bredd och indentering