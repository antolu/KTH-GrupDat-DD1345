n = 0
while n != 1729:
	a = int(input(" a = "))
	b = int(input(" b = "))
	print()

	n = a**3+b**3

	if n == 1729:
		print("Kubsumma = ",n)
		print("Programmering avslutad.")
		print()
	else:
		print("Kubsumma = ", n)
		print("Tyvärr, försök igen!")
		print()