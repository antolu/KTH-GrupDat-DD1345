def ram(h,b,t):
	for k in range(t):
		print(b*"*")
	for k in range(t,h-t):
		print(t*"*" + (b-2*t)*" " + t*"*")
	for k in range(h-t,h):
		print(b*"*")

print()
print("Vad är höjden, bredden, och ramtjocklecken?")
x = int(input(" Höjd = "))
y = int(input(" Bredd = "))
z = int(input(" Tjocklek = "))

print()

if z > y/2 or z > x/2:
	print("Felaktika parametrar!")
else:
	ram(x,y,z)	#Höjd, Bredd och tjocklek