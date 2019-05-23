from treenodeX2 import *

tree = binTree()
print(tree.height())     # bör ge 0
print(tree.isempty())    # bör ge True
tree.put('solen')
print(tree.isempty())    # bör ge False
print(tree.height())     # bör ge 1
tree.put('går')
tree.put('sin')
tree.put('höga')
tree.put('ban')
tree.put('uppå')
tree.put('himlarunden')
tree.put('månen')
tree.put('seglar')
tree.put('som')
tree.put('en')
tree.put('svan')
tree.put('uti')
tree.put('midnattsstunden')

print(tree.exists('visa'))     # bör ge False
print(tree.exists('ban'))      # bör ge True
tree.printtree()               # skriv ut sorterat
print(tree.height())           # ska ge 6 om insättningarna gjorts exakt enligt ovan
tree.delete('solen')
tree.printtree()
tree.delete('månen')
tree.printtree()
tree.delete('seglar')
tree.delete('månen')
tree.printtree()
tree.put('månen')
tree.printtree()
tree.put('solen')
tree.printtree()
tree.delete('uppå')
tree.printtree()