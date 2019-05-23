
	def __init__(self):
		from wordpair import Wordpair
		from queueADT import Queue
		wordlist = open('swahiliu.txt', encoding = 'utf8').read().split()

		glosor = Queue()

		for i in range(len(wordlist/2)):
		glosor.put(Wordpair(wordlist[2*i],wordlist[2*i+1]))


	def check(self):
		glosa = glosor.get()
		print("Vad betyder",glosa[0])
		test = input()

		if test = glosa[1]:
			if glosa.repeat():
			glosor.put(glosa)