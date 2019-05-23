from queue import Queue
import math

def radixsort(inputlist):
	length = len(inputlist)
	alist = Queue()
	buckets = []

	maxpower= int(math.log10(max(inputlist))) + 1

	for i in range(length):
		alist.put(inputlist[i])

	for x in range(10):								#skapa 10 "hinkar"
		buckets.append(Queue())

	for j in range(maxpower):						#upprepa för varje tiotal

		for k in range(length):						#sortera i hinkar
			tosort = alist.get()
			mod = (tosort // 10**j) % 10
			buckets[mod].put(tosort)

		for i in range(10):							#hämta talen från hinkarna och samla ihop dem, från minsta till största tal
			while not buckets[i].isempty():
				alist.put(buckets[i].get())

	res = []
	while not alist.isempty():						#skapa sorterad lista
		res.append(alist.get())

	return res
