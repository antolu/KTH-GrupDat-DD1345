def rektangel(a,b,c,d):
	for k in range(a):
		print(c*" " + b*d)

def ram(a,b,c,d):
	for k in range(c):
		print(b*d)
	for k in range(c,a-c+1):
		print(t*d + (b-2*c)*" " + c*d)
	for k in range(a-c,a):
		print(b*d)

def triangelBasNer(a,b,d):
		while a >= 1:
			print(b*" " + a*d)
			b +=1
			a -= 2

def triangelBasUpp(a,b,d):
	n=1
	while n <= a:
		print(int(b+(a-1)/2)*" " + n*d)
		b -=1
		n += 2

def romb(a,b,d):
	triangelBasUpp(a,b)
	triangelBasNer(a-2,b+1)

while True:
	print("Vilken figur ska ritas?")
	print("1. Rektangel")
	print("2. Ram")
	print("3. Triangel med bas neråt")
	print("4. Triangel med bas uppåt")
	print("5. Romb")
	print()

	program = input("")
	d = input(" Tecken som figuren ska ritas med: ")

	if program == "1":
		a = input(" Höjd: ")
		b = input(" Bredd: ")
		c = input(" Indentering: ")
		rektangel(a,b,c,"d")
		break
	elif program == "2":
		a = input(" Höjd: ")
		b = input(" Bredd: ")
		c = input(" Tjocklek på ramen: ")
		ram(a,b,c,"d")
		break
	elif program == "3":
		a = input(" Basbredd: ")
		b = input(" Indentering: ")
		triangelBasNer(a,b,"d")
		break
	elif program == "4":
		a = input(" Basbredd: ")
		b = input(" Indentering: ")
		triangelBasUpp(a,b,"d")
	elif program == "5":
		a = input(" Bredd: ")
		b = input(" Indentering: ")
		romb(a,b,"d")
