from treenode import binTree
import time

def ramanujan(talet):
	outputlist = []
	checklist = binTree()
	a = 0
	b = int(talet**(1/3))+1

	for i in range(int(talet**(1/3))):
		if a**3+b**3==talet and not checklist.exists(a) and a != b:
			outputlist.append((a,b))
			checklist.put(a)
		a += 1
		while b >= a:
			if a**3+b**3==talet and not checklist.exists(a) and a != b:
				outputlist.append((a,b))
				checklist.put(a)
			b -= 1
		b = int(talet**(1/3))+1

	return outputlist

def minstaramanujan(m):
	kubsummor = []
	tal = 1
	while len(kubsummor) < m:
		ram = ramanujan(tal)
		if len(ram) >= 2:
			kubsummor.append(str((tal,ram)))
		tal += 1

	return kubsummor

#talet = int(input("Talet: "))

#print(ramanujan(talet))

minstatal = int(input("Antal ramanujan-tal som söks: "))

start = time.time()
print("\n".join(minstaramanujan(minstatal)))
end = time.time()

print("Tiden: ", end-start, " sekunder.")