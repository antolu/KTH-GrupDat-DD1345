word15 = open("15wordu.txt", encoding = "utf-8").read().split()
word3u = open("word3u.txt", encoding = "utf-8").read().split()
english = open("englishu.txt", encoding = "utf-8").read().split()

import treenode

bintree1 = treenode.binTree()
bintree2 = treenode.binTree()
checklist = treenode.binTree()
budskap = []
budskap2 = []


for i in range(len(word15)):
	bintree1.put(word15[i])

for i in range(len(word3u)):
	if bintree2.exists(word3u[i]):
		budskap.append(word3u[i])
	bintree2.put(word3u[i])

for i in range(len(english)):
	ordet = english[i]
	if bintree2.exists(ordet) and not checklist.exists(ordet):
		budskap2.append(ordet)
		checklist.put(ordet)

print(bintree1.height())
print()
bintree1.printtree()
print()
print(" ".join(budskap))
print()
print(" ".join(budskap2))