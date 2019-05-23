class Wordpair:

	def __init__(self, l1, l2):
		self.lang1 = l1
		self.lang2 = l2
		self.ggr = 1

	def repeat(self):
		if self.ggr == 0:
			return False
		else:
			self.ggr -= 1
			return True

	def __str__(self):
		return str(self.lang1+"\n"+self.lang2)