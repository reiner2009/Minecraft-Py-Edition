import net.mcpy.world.block.Blocks as Blocks
from net.mcpy.world.block.Block import Block
import threading

class Chunk:
	def __init__(self, x, y, z):
		self.x=x
		self.y=y
		self.z=z
		self.blocks={}
		self.dirty=False
		self.lock=threading.Lock()
	def __eq__(self, other):
		if not isinstance(other, Chunk):
			return NotImplemented
		return (self.x==other.x and self.y==other.y and self.z==other.z)
	def __hash__(self):
		return hash((self.x, self.y, self.z))
	def getBlock(self, x,y,z):
		try:
			return self.blocks[(x,y,z)]
		except:
			return Blocks.AIR.create(x,y,z)
	def setBlock(self,x,y,z,block, update=False):
		if isinstance(block, Block):
			with self.lock:
				if block.id.path!="air":
					self.blocks[(x,y,z)]=block.create(x,y,z)
				else:
					self.blocks.pop((x,y,z),None)
				if update:
					self.dirty=True
	@staticmethod
	def parseBlockPos(x,y,z):
		return x // 8, y // 16, z // 8
