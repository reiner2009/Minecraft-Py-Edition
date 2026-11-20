from net.minecraft.world.chunk.Chunk import get_block, get_block_data
from net.minecraft.world.phys import AABB
import math
import threading
import time

def get_look_direction(ran, entity):
	world_x, world_y, world_z=entity.get_entity_position()
	yaw, pitch = entity.get_entity_facing()
	dx=world_x+(math.sin(math.radians(yaw))*math.cos(math.radians(pitch)))*ran
	dy=world_y-(math.sin(math.radians(pitch)))*ran
	dz=world_z-(math.cos(math.radians(yaw))*math.cos(math.radians(pitch)))*ran
	return dx ,dy, dz

def get_look_direction_as_d(entity):
