class treeNode():
	def __init__(self, item, left = None, right = None):
		self.item = item
		self.left = left
		self.right = right

	def childrenCount(self):
		counter = 0
		if self.left:
			counter += 1
		if self.right:
			coutner += 1
		return counter

	def lookup(self, key, parent = None):
		if key < self.item:
			if self.left is None:
				return None, None
			return self.left.lookup(key, self)
		elif key > self.item:
			if self.right is None:
				return None, None
			return self.right.lookup(key, self)
		else:
			return self, parent

def height(self):
	if self == None:
		return 0
	else:
		return 1 + max(height(self.left), height(self.right))

def inorder(root):
	if root == None:
		return []
	return inorder(root.left) + [root.item] + inorder(root.right)

class binTree():
	def __init__(self):
		self.root = None

	def put(self, key):
		if self.root == None:
			self.root = treeNode(key)
			return
		p = self.root		
		if not self.exists(key):

			while True:
				if key < p.item:
					if p.left == None:
						p.left = treeNode(key)
						return
					else:
						p = p.left
				elif key > p.item:
					if p.right == None:
						p.right = treeNode(key)
						return
					else:
						p = p.right
				else:
					return

	def exists(self, key):
		p = self.root
		if self.root == None:
			return False
		if key == p.item:
			return True
		while key != p.item and self.root != None:
			if key < p.item:
				if p.left == None:
					return False
				else:
					p = p.left
			elif key > p.item:
				if p.right == None:
					return False
				else:
					p = p.right
			if key == p.item:
				return True

	def delete(self, key):
		node, parent = self.lookup(key)
		if node is not None:
			childrenCount = node.childrenCount()
		if childrenCount == 0:
			if parent:
				if parent.left is node:
					parent.left = None
				else:
					parent.right = None
				del node
			else:
				self.item = None
		elif childrenCount == 1:
			if node.left:
				n = node.left
			else:
				n = node.right
			if parent:
				if parent.left is node:
					parent.left = n
				else:
					parent.right = n
				del node
			else:
				self.left = n.left
				self.right = n.right
				self.item = n.item
		else:
			parent = node
			successor = node.right
			while successor.left:
				parent = succcessor
				successor = successor.left
			node.item = sucessor.item
			if parent.left == successor:
				parent.eft = successor.right
			else:
				parent.right = successor.right

	def isempty(self):
		return self.root == None

	def height(self):
		return height(self.root)

	def printtree(self):
		print(inorder(self.root))