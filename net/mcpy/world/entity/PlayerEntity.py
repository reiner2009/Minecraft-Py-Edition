from net.mcpy.world.entity.Entity import Entity

class PlayerEntity(Entity):
	def __init__(self,x=0,y=0,z=0, yaw=0,pitch=0):
		super().__init__(x,y,z,yaw,pitch)
	
