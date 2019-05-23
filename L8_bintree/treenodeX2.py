class treeNode():
	def __init__(self, item, left = None, right = None):
		self.item = item
		self.left = left
		self.right = right

	def childrenCount(self):						# Returnerar antalet barn till noden
		counter = 0
		if self.left:
			counter += 1
		if self.right:
			counter += 1
		return counter

	def lookup(self, key, parent = None):			# Returnerar den sökta noden och dess förälder
		if key < self.item:
			if self.left is None:					# Om key är mindre än nuvarande self, men left är tom finns inte key!
				return None, None
			return self.left.lookup(key, self)		# Djupare i rekursionen, söker vänster delträd
		elif key > self.item:
			if self.right is None:
				return None, None
			return self.right.lookup(key, self)
		else:
			return self, parent

	def delete(self, key):
		node, parent = self.lookup(key)
		if node is not None:
			childrenCount = node.childrenCount()

		if childrenCount == 0:						# Om node inte har barn
			if parent:
				if parent.left is node:				# Om noden är till höger, ta bort den
					parent.left = None
				else:
					parent.right = None
				del node
			else:
				self.item = None 					# Om det är roten

		elif childrenCount == 1:					# Om noden har 1 barn
			if node.left:							# Ställer in pekaren n till barnet som har data
				n = node.left
			else:
				n = node.right
			if parent:								
				if parent.left is node:				# Om vänsta barnet till föräldern är noden som ska ersättas, ställ om pekaren till n
					parent.left = n
				else:
					parent.right = n
				del node
			else:									# Om det är roten (ingen förälder)
				self.left = n.left
				self.right = n.right
				self.item = n.item

		elif childrenCount == 2:					# Om noden har 2 barn
			parent = node 							# Förflyttar sig ner i trädet, så att noden blir föräldern
			successor = node.right					# Använder höger gren för att ersätta noden
			while successor.left != None:			# Förflyttar sig till den minsta noden i grenen
				parent = successor
				successor = successor.left
			node.item = successor.item				# Byter ut data i noden som ska ersättas
			if parent.left == successor:			
				parent.left = successor.right
			else:
				parent.right = successor.right

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
		if self.exists(key):
			self.root.delete(key)
		else: 
			print('Something went wrong here!')

	def isempty(self):
		return self.root == None

	def height(self):
		def heightHelper(self):
			if self == None:
				return 0
			else:
				return 1 + max(heightHelper(self.left), heightHelper(self.right))
		return heightHelper(self.root)

	def printtree(self):
		def inorder(root):
			if root == None:
				return []
			return inorder(root.left) + [root.item] + inorder(root.right)
		print(inorder(self.root))