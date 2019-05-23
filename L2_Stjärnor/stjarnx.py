def rektangel(a,b,c,d):
	figur = []
	for k in range(a):
		figur.append(c*" " + b*d)
		#print(c*" " + b*d)
	return figur.join(\n )

#rektangel(4,5,10,"*") #Höjd, bredd, indentering och tecken

def ram(h,b,t):
	for k in range(t):
		print(b*"*")
	for k in range(t,h-t):
		print(t*"*" + (b-2*t)*" " + t*"*")
	for k in range(h-t,h):
		print(b*"*")

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

#romb(9,10) #Maxbredd + 2 och indentering