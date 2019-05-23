from treenode import *
from queueADT import *
import time

word3u = open("word3u.txt", encoding = "utf-8").read().split()
wordlist = set()
for i in range(len(word3u)):
	wordlist.add(word3u[i])

alphabet = list("abcdefghijklmnopqrstuvwxyzåäö")

class Word():
	def __init__(self, theword, parent = None):
		self.word = theword
		self.parent = parent

class Queue():
	def __init__(self):
		self.alist = []
	def put(self,newdata):
		self.alist.append(newdata)
	def get(self):
		return self.alist.pop(0)
	def isEmpty(self):
		return self.alist == []
	def length(self):
		return len(self.alist)
	def out(self):
		return self.alist

def genChild(theword):
	output = Queue()

	for i in range(3):
		for k in range(29):
			ordet = list(theword.word)
			ordet[i] = alphabet[k]
			newword = Word("".join(ordet))
			newword.parent = theword

			if newword.word in wordlist and newword.word != theword.word:
				output.put(newword)

	return output

def longestPath(childlist,s):
	start = Word(s)

	q = Queue()
	usedWords = set()

	q.put(start)

	while not q.isEmpty():
		tempword = q.get()

		idx = word3u.index(tempword.word)
		z = childlist[idx].out()

		for i in range(len(z)):
			if z[i].word not in usedWords:
#				print(z[i].word)
				q.put(z[i])
				usedWords.add(z[i].word)

	return z

def BFS(s, e):
	start = Word(s)
	end = Word(e)
	q = Queue()
	usedWords = set()
	q.put(start)

	while not q.isEmpty():
		tempword = q.get()

		if tempword.word == end.word:
			return pathToWord(s,tempword)
			break

		usedWords.add(tempword.word)
		z = genChild(tempword).out()

		for i in range(len(z)):
			if z[i].word not in usedWords:
				q.put(z[i])
				usedWords.add(z[i].word)

	return False

def pathToWord(s,theword):
	output = []

	while theword.parent != None:
		output.append(theword.word)
		theword = theword.parent
	output.append(s)
	return " -> ".join(list(reversed(output)))

def BFSX(ordet):
	childlist = []

	for i in range(len(word3u)):
		childlist.append(genChild(Word(word3u[i])))

	ord2 = []

	ord1 = longestPath(childlist, ordet)
	for i in range(len(ord1)):
		ord2.append(longestPath(childlist, ord1[i].word))

	output = []
	for i in range(len(ord1)):
		for k in range(len(ord2[i])):
			output.append(BFS(ord1[i].word, ord2[i][k].word))

	return "\n".join(output)

ordet = input("Ordet: ")

start = time.time()

print(BFSX(ordet))

end = time.time()

print()
print("Tiden: ", end-start," sekunder")
