from net.minecraft.entity.PathFinderMob import PathFinderMob
import net.minecraft.client.render.entity.PigRenderer as PigRenderer
from net.minecraft.entity.ai.Goal import RandomStrollAroundGoal

class PigEntity(PathFinderMob):
	def __init__(self, name_tag_is_visible=True):
		super().__init__(name_tag_is_visible)
		self.targetSelector.addBehaviourGoal(0, RandomStrollAroundGoal, 1)
	def tick(self):
		super().tick()
		PigRenderer.render_body_layer(self.x, self.y, self.z, self.yaw, self.pitch, 0, 0)
