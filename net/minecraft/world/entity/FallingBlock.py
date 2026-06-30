from net.minecraft.world.entity.Entity import Entity
from net.minecraft.world.chunk.Chunk import get_block

class FallingBlock(Entity):
	def __init__(self):
		super().__init__()
	def tick(self):
		if get_block(round(self.x),round(self.y, 1)-1,round(self.z))=="air":
			self.y-=0.1
