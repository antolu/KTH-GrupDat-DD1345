import time

#Initiera filer och lägg alla ord i en mängd

word3u = open("word3u.txt", encoding = "utf-8").read().split()
wordlist = set()
for i in range(len(word3u)):
	wordlist.add(word3u[i])

#Skapa ett alfabet
alphabet = list("abcdefghijklmnopqrstuvwxyzåäö")

#################################################
#	Ordklass med .word som ordet och .parent	#
#	är en länk pekare till föräldern.			#
#################################################

class Word():
	def __init__(self, theword, parent = None):
		self.word = theword
		self.parent = parent
		self.path = 0

	def pathLength(self):
		counter = 0
		while self != None:
			counter += 1
			self = self.parent
		return counter

#################################################
#	Köklass med vanliga funktioner. 			#
#################################################

class Queue():
	def __init__(self):
		self.alist = []

	def put(self,newdata):
		self.alist.append(newdata)

	def get(self):
		return self.alist.pop(0)

	def isEmpty(self):
		return self.alist == []

#################################################
#	Funktion som genererar barn till input-ord 	#
# 	mha permutationer och returnerar lista		#
#################################################

def genChild(theword):
	output = []

	for i in range(3):
		for k in range(29):
			ordet = list(theword)
			ordet[i] = alphabet[k]
			newword = "".join(ordet)

			if newword in wordlist and newword != theword:
				output.append(newword)

	return output

#################################################
#	Funktion som hittar ordet som ligger längst	#
#	bort från ordet s. 							#
#################################################

def longestPath(s, children):
	start = Word(s)

	q = Queue()

	q.put(start)
	usedWords = set()
	usedWords.add(s)
	out = []

#################################################
#	Hämta ord ur kön, hitta dess barn i ett		#
#	dictionary, sätt barnens förälder tll ordet	#
#	och lägg oanvända ord i kön igen			#
#################################################

	while not q.isEmpty():
		tempword = q.get()
		tempChildren = children[tempword.word]
		childlist = []

		for i in range(len(tempChildren)):
			childlist.append(Word(tempChildren[i], tempword))

		for i in range(len(childlist)):
			if childlist[i].word not in usedWords:
				out = []
				q.put(childlist[i])
				usedWords.add(childlist[i].word)
				out.append(childlist[i])
#################################################
#	När kön är tom returneras en en lista med 	#
#	ord som ligger längst bort och hur långt 	#
#	bort de ligger 								#
#################################################

	if out != []:
		paths = []
		for i in range(len(out)):
			paths.append(pathToWord(out[i]))
		return "\n".join(paths), out[0].pathLength()
	else:
		return pathToWord(tempword), tempword.pathLength()

#################################################
#	Funktion som backtrackar ordet med parent- 	#
#	pekaren och returnerar en sträng med vägen 	#
#################################################

def pathToWord(theword):
	output = []

	while True:
		output.append(theword.word)
		if theword.parent == None:
			break
		theword = theword.parent
	return " -> ".join(list(reversed(output)))

#################################################
#	Skapa dicitonary med barn och kända vägar 	#
#	för varje ord i word3u, hitta vägen som är 	#
#	längst med "max", returnera sträng med de	#
#	vägarna som är längst. 						#
#################################################

def BFSX():
	children = {}
	knownPaths = {}

	for k in range(len(word3u)):
		children[word3u[k]] = genChild(word3u[k])

	for i in range(len(word3u)):
		path, pathlength = longestPath(word3u[i], children)
		knownPaths[path] = pathlength

	longestpath = max(knownPaths.values())

	revdict = {}
	for key, value in knownPaths.items():
		revdict[value] = revdict.get(value, [])
		revdict[value].append(key)

	return "\n".join(revdict[longestpath])

#################################################
#	Kör funktionen mec timer. 					#
#################################################

start = time.time()

z = BFSX()
print(z)

end = time.time()

print()
print("Tiden: ", end-start," sekunder")
