import math

def get_look_direction_behind(ran, entity):
	world_x, world_y, world_z=entity.get_entity_position()
	yaw, pitch = entity.get_entity_facing()
	dx = world_x - (math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))) * ran
	dy = world_y + (math.sin(math.radians(pitch))) * ran
	dz = world_z + (math.cos(math.radians(yaw)) * math.cos(math.radians(pitch))) * ran
	return dx, dy, dz

def get_look_direction_front(ran, entity):
	world_x, world_y, world_z=entity.get_entity_position()
	yaw, pitch = entity.get_entity_facing()
	dx = world_x + (math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))) * ran
	dy = world_y - (math.sin(math.radians(pitch))) * ran
	dz = world_z - (math.cos(math.radians(yaw)) * math.cos(math.radians(pitch))) * ran
	return dx, dy, dz