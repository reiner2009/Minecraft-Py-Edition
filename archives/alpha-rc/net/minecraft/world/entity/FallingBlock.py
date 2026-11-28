from net.minecraft.world.entity.Entity import Entity
from net.minecraft.world.chunk.Chunk import get_block
from net.minecraft.util import Override

class FallingBlock(Entity):
	def __init__(self):
		super().__init__()
	@Override
	def tick(self):
		if get_block(round(self.x),round(self.y, 1)-1,round(self.z))=="air":
			self.y-=0.1
