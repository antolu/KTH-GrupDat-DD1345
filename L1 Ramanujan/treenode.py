class treeNode():
	def __init__(self, item, left = None, right = None):
		self.item = item
		self.left = left
		self.right = right

def height(self):
	if self == None:
		return 0
	else:
		return 1 + max(height(self.left), height(self.right))

def inorder(root):
	if root == None:
		return []
	return inorder(root.left)  + inorder(root.right) + [root.item]

def postorder(root):
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

	def isempty(self):
		return self.root == None

	def height(self):
		return height(self.root)

	def printtree(self):
		return inorder(self.root)