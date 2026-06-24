from net.minecraft.entity.Entity import Entity

class LivingEntity(Entity):
	def __init__(self, name_tag_is_visible=True):
		super().__init__()
		self.name_tag_is_visible=name_tag_is_visible
		self.mainhand_item=None
		self.walk_pitch_direction = 0
	def swing(self, arm):
		pass
	def setMainhandItem(self, item):
		self.mainhand_item=item
	def getMainhandItem(self):
		return self.mainhand_item
