class Queue():
	def __init__(self):
		self.alist = []

	def put(self, inputdata):
		self.alist.append(inputdata)

	def get(self):
		if self.isempty():
			return
		else:
			return self.alist.pop(0)

	def isempty(self):
		if self.alist == []:
			return True
		else:
			return False
