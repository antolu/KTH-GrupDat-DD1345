from treenode import *
from queueADT import *

word3u = open("word3u.txt", encoding = "utf-8").read().split()
wordlist = binTree()
for i in range(len(word3u)):
	wordlist.put(word3u[i])

alphabet = list("abcdefghijklmnopqrstuvwxyzåäö")

class Word():
	def __init__(self, theword, parent = None):
		self.word = theword
		self.parent = parent

def genChild(theword):
	output = []

	for i in range(3):
		for k in range(29):
			ordet = list(theword.word)
			ordet[i] = alphabet[k]
			newword = Word("".join(ordet))
			newword.parent = theword

			if wordlist.exists(newword.word) and newword.word != theword.word:
				output.append(newword)

	return output

def BFS(s, e):
	start = Word(s)
	end = Word(e)
	q = Queue()
	checklist = binTree()
	q.put(start)

	while not q.isempty():
		tempword = q.get()

		if tempword.word == end.word:
			return pathToWord(s,tempword)
			break

		checklist.put(tempword.word)
		z = genChild(tempword)

		for i in range(len(z)):
			if not checklist.exists(z[i].word):
				q.put(z[i])
				checklist.put(z[i].word)

	return False

def pathToWord(s,theword):
	output = []
	while theword.parent != None:
		output.append(theword.word)
		theword = theword.parent
	output.append(s)
	return " -> ".join(list(reversed(output)))

print(BFS("dum","vis"))
print(BFS("blå","röd"))
print(BFS("fan","gud"))
print(BFS("öva","klä"))