from net.minecraft.world.chunk.Chunk import get_block
import math

def get_look_direction(ran, entity):
	world_x, world_y, world_z=entity.get_entity_position()
	yaw, pitch = entity.get_entity_facing()
	dx=round(world_x+(math.sin(math.radians(yaw))*math.cos(math.radians(pitch)))*ran)
	dy=round(world_y-(math.sin(math.radians(pitch)))*ran)
	dz=round(world_z-(math.cos(math.radians(yaw))*math.cos(math.radians(pitch)))*ran)
	return dx ,dy, dz

def get_pos(entity):
	world_x, world_y, world_z=entity.get_entity_position()
	ran=1
	while get_block(*get_look_direction(ran, entity))=="air" and ran < 5:
		ran+=1
	pran=ran-1
	if get_neighbour_block(*get_look_direction(pran, entity))==False:
		pran=0
		while pran < 6 and get_neighbour_block(*get_look_direction(pran, entity))==False:
			pran+=1
	px,py,pz=get_look_direction(pran, entity)
	if get_block(round(world_x), round(world_y), round(world_z))!="air":
		bx,by,bz=round(world_x), round(world_y), round(world_z)
	elif get_block(*get_look_direction(ran, entity))!="air":
		bx,by,bz=get_look_direction(ran, entity)
	else:
		bx,by,bz=None, None, None
	return px,py,pz,bx,by,bz

def get_neighbour_block(X,Y,Z):
	if get_block(X,Y,Z) =="air" and (get_block(X+1,Y,Z)!= "air" or get_block(X,Y+1,Z)!= "air" or get_block(X,Y,Z+1)!= "air" or get_block(X-1,Y,Z)!= "air" or get_block(X,Y-1,Z)!= "air" or get_block(X,Y,Z-1)!= "air"):
		return True
	else:
		return False
