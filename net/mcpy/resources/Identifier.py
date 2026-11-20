class Identifier:
	def __init__(self, namespace="minecraft", path="path"):
		self.namespace=namespace
		self.path=path
	def getAsString(self):
		return self.namespace+":"+self.path
