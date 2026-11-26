from net.mcpy.world.entity.Entity import Entity
import net.mcpy.world.block.Blocks as Blocks
import math

class PlayerEntity(Entity):
	def __init__(self,x=0,y=0,z=0, yaw=0,pitch=0):
		super().__init__(x,y,z,yaw,pitch)
	def getLookDirection(self, ran):
		dx = self.x + (math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))) * ran
		dy = self.y + (math.sin(math.radians(self.pitch))) * ran
		dz = self.z + (math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))) * ran
		return dx, dy, dz
	def getLookDirectionVector(self):
		dx = (math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)))
		dy = (math.sin(math.radians(self.pitch)))
		dz = (math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)))
		return dx, dy, dz
	def getTMax(self, pos, block, direction):
		if direction > 0:
			return (block + 1 - pos) / direction
		elif direction < 0:
			return (pos - block) / -direction
		return math.inf
	def getTrackedPos(self, level):
		ran=0
		dx,dy,dz=self.getLookDirectionVector()
		ox,oy,oz=self.getPos()
		map_x=math.floor(ox)
		map_y=math.floor(oy)
		map_z=math.floor(oz)
		step_x=1 if dx > 0 else -1
		step_y=1 if dy > 0 else -1
		step_z=1 if dz > 0 else -1
		delta_x=1/abs(dx) if dx != 0 else math.inf
		delta_y=1/abs(dy) if dy != 0 else math.inf
		delta_z=1/abs(dz) if dz != 0 else math.inf
		max_x=self.getTMax(ox, map_x, dx)
		max_y=self.getTMax(oy, map_y, dy)
		max_z=self.getTMax(oz, map_z, dz)
		normal=(None, None, None)
		while ran<5 and (level.getBlock(map_x, map_y, map_z)==Blocks.AIR or level.getBlock(map_x, map_y, map_z)==Blocks.VOID):
			ran+=1
			if max_x < max_y and max_x < max_z:
				map_x+=step_x
				max_x+=delta_x
				normal=(-step_x, 0, 0)
			elif max_y < max_z:
				map_y+=step_y
				max_y+=delta_y
				normal=(0, -step_y, 0)
			else:
				map_z+=step_z
				max_z+=delta_z
				normal=(0,0,-step_z)
		nx,ny,nz=normal
		if level.getBlock(map_x, map_y, map_z)==Blocks.AIR or level.getBlock(map_x, map_y, map_z)==Blocks.VOID:
			normal=(None, None, None)
		if normal!=(None, None, None):
			return map_x+nx, map_y+ny, map_z+nz, map_x, map_y, map_z
		else:
			return *normal, map_x, map_y, map_z
