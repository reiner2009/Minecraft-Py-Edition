from net.minecraft.world.entity.FallingBlock import FallingBlock
from net.minecraft.world.chunk.Chunk import explode
from net.minecraft.util import Override

class IgnitedTnt(FallingBlock):
	def __init__(self, c=5):
		super().__init__()
		self.countdown=c*60
		self.v=489
	def set_sound_volume(self, v):
		self.v=v
	@Override
	def tick(self):
		from net.minecraft.client.render.world.entity.IgnitedTntRenderer import renderIgnitedTnt
		super().tick()
		renderIgnitedTnt(*self.get_entity_position(), self.countdown)
		self.countdown-=1
		if self.countdown<=0:
			explode(*self.get_entity_position(), 4, self.v)
			self.discard()
