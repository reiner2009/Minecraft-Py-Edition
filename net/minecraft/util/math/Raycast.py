from net.minecraft.world.chunk.Chunk import get_block, get_block_data
from net.minecraft.world.phys import AABB
import math

def get_look_direction(ran, entity):
	world_x, world_y, world_z=entity.get_entity_position()
	yaw, pitch = entity.get_entity_facing()
	dx=world_x+(math.sin(math.radians(yaw))*math.cos(math.radians(pitch)))*ran
	dy=world_y-(math.sin(math.radians(pitch)))*ran
	dz=world_z-(math.cos(math.radians(yaw))*math.cos(math.radians(pitch)))*ran
	return dx ,dy, dz

def get_pos(entity):
	ran=0
	bx,by,bz=None, None, None
	px,py,pz=None, None, None
	x,y,z=entity.get_entity_position()
	while ran <= 5 and not (get_block(x,y,z)!="air" and get_block_data(x,y,z).getCollisionShape().intersects(AABB(x,y,z,x,y,z))):
		ran+=0.01
		x,y,z=get_look_direction(ran, entity)
	bx=round(x)
	by=round(y)
	bz=round(z)
	return px,py,pz,bx,by,bz
