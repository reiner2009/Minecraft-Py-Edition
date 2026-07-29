from net.minecraft.world.entity.FallingBlock import FallingBlock
from net.minecraft.client.render.world.entity.FallingBlockRenderer import renderFallingBlock
from net.minecraft.world.chunk.Chunk import get_block, set_block, reload_chunks
from net.minecraft.util import Override

class FallingGravel(FallingBlock):
	def __init__(self):
		super().__init__()
	@Override
	def tick(self):
		super().tick()
		renderFallingBlock(*self.get_entity_position(), "gravel")
		if get_block(round(self.x),round(self.y, 1)-1,round(self.z))!="air":
			set_block(round(self.x),round(self.y),round(self.z), "gravel")
			reload_chunks()
			self.discard()
