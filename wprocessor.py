class Document(object):
	"""Basic document Class"""
	def __init__(self):
		self.characters = []
		self.cursor = 0
		self.filename = ''

	def insert(self,character):
		self.characters.insert(self.cursor, character)
		self.cursor += 1

	def delete(self):
		del self.characters[self.cursor]

	def save(self):
		f = open(self.filename, 'w')
		f.write("".join(self.characters))
		f.close()

	def foward(self):
		self.cursor += 1

	def back(self):
		self.cursor -= 1