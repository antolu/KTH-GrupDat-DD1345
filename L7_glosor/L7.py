from wordpair import Wordpair
#from queueADT import Queue
from nodequeue import *

with open("swahiliu.txt", encoding = 'utf8') as ins:
	wordlist = ins.read().splitlines()

glosor = Queue()

for i in range(len(wordlist)//2):
	glosor.put(Wordpair(wordlist[2*i],wordlist[2*i+1]))

print("Välkommen till glosförhöret!")

while not glosor.isempty():
	tempglosa = glosor.get()
	glosa = str(tempglosa).splitlines()

	test = input(str("Vad betyder "+glosa[1]+"? "))

	if str(test) == str(glosa[0]):
		print("Rätt")
		if tempglosa.repeat():
			glosor.put(tempglosa)
	else:
		print("Fel! Försök igen senare!")
		print("Borde ha varit ",glosa[0])
		glosor.put(tempglosa)

	print()

print("Glosförhöret slutfört!")
