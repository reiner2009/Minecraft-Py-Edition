from net.mcpy.world.entity.Entity import Entity
import math

class PlayerEntity(Entity):
	def __init__(self,x=0,y=0,z=0, yaw=0,pitch=0):
		super().__init__(x,y,z,yaw,pitch)
	def getTrackedPos(self):
		ran=4
		dx = self.x + (math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))) * ran
		dy = self.y + (math.sin(math.radians(self.pitch))) * ran
		dz = self.z + (math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))) * ran
		return round(dx), round(dy), round(dz)
