class treeNode():
	def __init__(self, item, parent = None, left = None, right = None):
		self.item = item
		self.parent = parent
		self.left = left
		self.right = right

class binTree():
	def __init__(self):
		self.root = None

	def put(self, key):
		if self.root == None:
			self.root = treeNode(key)
		else:
			if not self.exists(key):
				if key < self.pos.item:
					self.posKid = treeNode(key, self.pos)
					self.pos.left = self.posKid
				elif key > self.pos.item:
					self.posKid = treeNode(key, self.pos)
					self.pos.right = self.posKid

	def exists(self, key):
		if findPar(key) != None, None:
			return True
		else:
			self.pos, self.posKid = findPar(key)
			return False

	def findPar(self, key):
		p = self.root
		if p == None:
			return False
		while True:
			if key < p.item:
				if p.left == None:
					return p, p.left
				else:
					p = p.left
			elif key > p.item:
				if p.right == None:
					return p, p.right
				else:
					p = p.right
			elif p.item == key:
				return p.parent, p

	def remove(self, key):
		def small(aroot):
			p = aroot
			while p.left != None:
				p = p.left
			return p

		def big(aroot):
			p = aroot
			while p.right != None:
				p = p.right
			return p

		def maxOneKid(aroot):
			return aroot.left != None and aroot.right == None or aroot.left == None and aroot.right != None

		def theKid(aroot):
			if maxOneKid(aroot):
				if aroot.left == None and aroot.right != None:
					return aroot.right
				elif aroot.right == None and aroot.left != None:
					return aroot.left
				else:
					return None

		def removeNode(parent, element):
			if parent.left == None:
				parent.right = None
			elif parent.right == None:
				parent.left = None

		def replace(parent, thekid):
			if thekid.item < parent:
				parent.left = thekid
				thekid.parent = parent
			elif thekid.item > parent:
				parent.right = thekid
				thekid.parent = parent

		parent, element = self.findPar(key)
		if element == None:
			return
		if maxOneKid(element):
			thekid = theKid(element)
			if thekid == None:
				removeNode(parent, element)
			else:
				removeNode(parent, element)
				replace(parent, thekid)
		elif not maxOneKid(element):
			



	def isempty(self):
		return self.root == None

	def height(self):
		def height(self):
			if self == None:
				return 0
			else:
				return 1 + max(height(self.left), height(self.right))

		return height(self.root)

	def printtree(self):
		def inorder(root):
			if root == None:
				return []
			return inorder(root.left) + [root.item] + inorder(root.right)

		print(inorder(self.root))