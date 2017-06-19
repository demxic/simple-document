class Cursor(object):
	"""Basic cursor that knows its position and moves itsel relative to it"""
	def __init__(self, document):
		self.document = document
		self.position = 0

	def forward(self):
		self.position += 1

	def back(self):
		self.position -= 1

	def home(self):
		while self.document.characters[self.position-1] !='\n' :
			self.back()
			if self.position == 0:
				#Got to beginning of file before new line
				break

	def end(self):
		while self.position < len(self.document.characters) and self.document.characters[self.position] !='\n':
			self.forward()

class Document(object):
	"""Basic document Class"""
	def __init__(self):
		self.characters = []
		self.cursor = Cursor(self)
		self.filename = ''

	def insert(self,character):
		self.characters.insert(self.cursor.position, character)
		self.cursor.forward()

	def delete(self):
		del self.characters[self.cursor.position]

	def save(self):
		f = open(self.filename, 'w')
		f.write("".join(self.characters))
		f.close()

