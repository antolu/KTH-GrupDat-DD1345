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

def romb(a,b):
	triangelBasUpp(a,b)
	triangelBasNer(a-2,b+1)

romb(9,10) #Maxbredd + 2 och indentering