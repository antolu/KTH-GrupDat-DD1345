def rektangel(a,b,c,d):
	figur = []
	for k in range(a):
		figur.append(c*" " + b*d)
	return "\n".join(figur)

#rektangel(4,5,10,"*") #Höjd, bredd, indentering och tecken

def ram(h,b,t):
	figur = []
	for k in range(t):
		figur.append(b*"*")
	for k in range(t,h-t):
		figur.append(t*"*" + (b-2*t)*" " + t*"*")
	for k in range(h-t,h):
		figur.append(b*"*")
	return "\n".join(figur)

def triangelBasNer(a,b):
	figur = []
	while a >= 1:
		figur.append(b*" " + a*"*")
		b +=1
		a -= 2
	return "\n".join(figur)

def triangelBasUpp(a,b):
	n=1
	figur = []
	while n <= a:
		figur.append(int(b+(a-1)/2)*" " + n*"*")
		b -=1
		n += 2
	return "\n".join(figur)

def romb(a,b):
	return triangelBasUpp(a,b) + "\n" + triangelBasNer(a-2,b+1)


#romb(9,10) #Maxbredd + 2 och indentering