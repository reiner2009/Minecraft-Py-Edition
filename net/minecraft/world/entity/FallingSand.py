from net.minecraft.world.entity.FallingBlock import FallingBlock
from net.minecraft.client.render.world.entity.FallingBlockRenderer import renderFallingBlock
from net.minecraft.world.chunk.Chunk import get_block, set_block, reload_chunks
from net.minecraft.util import Override

class FallingSand(FallingBlock):
	def __init__(self):
		super().__init__()
	@Override
	def tick(self):
		super().tick()
		renderFallingBlock(*self.get_entity_position(), "sand")
		if get_block(round(self.x),round(self.y, 1)-1,round(self.z))!="air":
			set_block(round(self.x),round(self.y),round(self.z), "sand")
			reload_chunks()
			self.discard()
