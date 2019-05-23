class Node:
	def __init__(self, item = None, nextitem = None):
		self.item = item
		self.next = nextitem

class Queue():
	def __init__(self):
		self.top = None
		self.last = None

	def put(self, inputdata):
		if self.isempty():
			self.top = Node(inputdata)
			self.last = self.top
			self.top.next = self.last
		else:
			self.last.next = Node(inputdata)
			self.last = self.last.next

	def get(self):
		if self.isempty():
			return None
		else:
			out = self.top.item
			if self.top == self.last:
				self.last = None
				return self.top.item

			self.top = self.top.next
			return out
			

	def isempty(self):
		if self.last == None:
			return True
		else:
			return False
