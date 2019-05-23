dictionary = open('ordlistau.txt', encoding = 'utf8').read().split()

def linsok(word):
	check = 0
	for i in range(len(dictionary)):
		if dictionary[i] == word:
			print(word + " finns")
			check += 1
			break
	if check != 0:
		print(word + " finns inte")

def wordinput():
	while True:
		word = input("Ditt ord: ")
		linsok(word)

wordinput()

ord[1], ord[2], ord[3], ord[4], ord[5] = ord[3], ord[4], ord[5], ord[1], ord[2]