from net.minecraft.entity.Entity import Entity
from net.minecraft.world.chunk.Chunk import explode
from net.minecraft.client.render.entity.PrimedTntRenderer import*

class PrimedTnt(Entity):
	def __init__(self):
		super().__init__()
		self.countdown=5*60
		self.v=489
	def set_sound_volume(self, v):
		self.v=v
	def tick(self):
		renderPrimedTnt(*self.get_entity_position(), self.countdown)
		self.countdown-=1
		if self.countdown<=0:
			explode(*self.get_entity_position(), 4, self.v)
			self.discard()
