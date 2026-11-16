from net.mcpy.resources.ResourceLocation import ResourceLocation
import threading
import math

class Chunk:
	def __init__(self, x, z):
		self.x=x
		self.z=z
		self.blocks={}
		self.air=ResourceLocation(path="air")
		self.dirty=True
		self.lock=threading.Lock()
	def __eq__(self, other):
		if not isinstance(other, Chunk):
			return NotImplemented
		return (self.x==other.x and self.z==other.z)
	def __hash__(self):
		return hash((self.x, self.z))
	def getBlock(self, x,y,z):
		try:
			return self.blocks[(x,y,z)]
		except:
			return self.air
	def setBlock(self,x,y,z,resource_location):
		with self.lock:
			if resource_location.path!="air":
				self.blocks[(x,y,z)]=resource_location
			else:
				self.blocks.pop((x,y,z),None)
			self.dirty=True
	@staticmethod
	def parseBlockPos(x,y,z):
		return x // 8, z // 8
