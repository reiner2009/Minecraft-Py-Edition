from net.minecraft.world.chunk.Chunk import *
import net.minecraft.util.Logger as logger
import net.minecraft.world.chunk.Chunk as chunk
import net.minecraft.world.entity.Entities as Entities
from net.minecraft.chat.Chat import *
from net.minecraft.world.Time import set_tick, get_time
import traceback
import net.minecraft.resources.DataLocation as DataLocation

def irange(o,t):
	t=int(t)
	o=int(o)
	t=t-1
	if t < o:
		for i in range(o, t, -1):
			yield i
	elif t > o:
		t=t+2
		for i in range(o, t):
			yield i
	else:
		for i in range(o,t):
			yield i


def string_to_position(string, entity):
	global world_x, world_y, world_z
	world_x, world_y, world_z=entity.get_entity_position()
	if string.split()[1].startswith("~"):
		try:
			x=round(world_x+float(string.split()[1][1:]))
		except:
			x=round(world_x)
	else:
		x=float(string.split()[1])
	if string.split()[2].startswith("~"):
		try:
			y=round(world_y+float(string.split()[2][1:]))
		except:
			y=round(world_y)
	else:
		y=float(string.split()[2])
	if string.split()[3].startswith("~"):
		try:
			z=round(world_z+float(string.split()[3][1:]))
		except:
			z=round(world_z)
	else:
		z=float(string.split()[3])
	return x,y,z
	
def string_to_position_for_fill(string, entity):
	global world_x, world_y, world_z
	world_x, world_y, world_z=entity.get_entity_position()
	if string.split()[1].startswith("~"):
		try:
			x=round(world_x+float(string.split()[1][1:]))
		except:
			x=round(world_x)
	else:
		x=float(string.split()[1])
	if string.split()[2].startswith("~"):
		try:
			y=round(world_y+float(string.split()[2][1:]))
		except:
			y=round(world_y)
	else:
		y=float(string.split()[2])
	if string.split()[3].startswith("~"):
		try:
			z=round(world_z+float(string.split()[3][1:]))
		except:
			z=round(world_z)
	else:
		z=float(string.split()[3])
	if string.split()[4].startswith("~"):
		try:
			x1=round(world_x+float(string.split()[4][1:]))
		except:
			x1=round(world_x)
	else:
			x1=float(string.split()[4])
	if string.split()[5].startswith("~"):
		try:
			y1=round(world_y+float(string.split()[5][1:]))
		except:
			y1=round(world_y)
	else:
		y1=float(string.split()[5])
	if string.split()[6].startswith("~"):
		try:
			z1=round(world_z+float(string.split()[6][1:]))
		except:
			z1=round(world_z)
	else:
		z1=float(string.split()[6])
	return x,y,z,x1,y1,z1

def teleport(x,y,z, entity):
	entity.spawn(x,y,z)

def assume_command(string, entity):
	try:
		if string.split()[0]=="/setblock":
			set_block(*string_to_position(string, entity), string.split()[4])
			reload_chunks()
			show_text(f"block in {string_to_position(string, entity)} successfully replaced", [255,255,255,255])
			logger.set_environment("Main")
			logger.info(f"[COMMAND] block in {string_to_position(string, entity)} successfully replaced")
			logger.set_environment("Client")
		elif string.split()[0]=="/list_blocks" or string.split()[0]=="/listblocks":
			for id_name in blocks:
				show_text(id_name, [255,255,255,255])
		elif string.split()[0]=="/fill":
			a=0
			x,y,z,x1,y1,z1=string_to_position_for_fill(string, entity)
			for x2 in irange(x,x1):
				for y2 in irange(y,y1):
					for z2 in irange(z,z1):
						set_block(x2,y2,z2, string.split()[7])
						a+=1
			reload_chunks()
			show_text(f"{a} blocks successfully replaced", [255,255,255,255])
			logger.set_environment("Main")
			logger.info(f"[COMMAND] {a} blocks successfully replaced")
			logger.set_environment("Client")
		elif string.split()[0]=="/tp" or string.split()[0]=="/teleport":
			teleport(*string_to_position(string, entity), entity)
			show_text(f"Teleported {Playername.playername} to {string_to_position(string, entity)}", [255, 255, 255, 255])
			logger.set_environment("Main")
			logger.info(f"[COMMAND] Teleported {Playername.playername} to {string_to_position(string, entity)}")
			logger.set_environment("Client")
		elif string.split()[0]=="/reset_world":
			chunk.create_new_world()
			reload_chunks()
			show_text("World successfully reset ", [255, 255, 255, 255])
			logger.set_environment("Main")
			logger.info("[COMMAND] World successfully reset")
		elif string.split()[0]=="/summon":
			x,y,z=string_to_position(string, entity)
			entityName=string.split()[4]
			try:
				entity=Entities.entities[entityName](True)
			except:
				entity=Entities.entities[entityName]()
			entity.spawn(x,y,z)
			try:
				entity.setName(string.split()[5])
			except:
				entity.setName("Steve")
			try:
				entity.setSkin(string.split()[6])
			except:
				try:
					entity.setSkin(DataLocation.get_resource_path("assets/minecraft/textures/entity/player/steve.png"))
				except:
					pass
			entity.set_thirt_person_perspective()
			logger.info(f"[COMMAND] Added {entityName} successfully at {string_to_position(string, entity)}")
			show_text(f"Added {entityName} successfully at {string_to_position(string, entity)}", [255, 255, 255, 255])
		elif string.split()[0]=="/time":
			try:
				if string.split()[1]=="set":
					if string.split()[2]=="day":
						set_tick(6*60)
					elif string.split()[2]=="night":
						set_tick(18*60)
					else:
						set_tick(float(string.split()[2])*60)
					logger.info(f"[COMMAND] Time set to {get_time()}")
					show_text(f"Time set to {get_time()}", [255, 255, 255, 255])
			except:
				logger.info(f"[COMMAND] Current time: {get_time()}")
				show_text(f"Current time: {get_time()}",[255, 255, 255, 255])
		elif string.split()[0] == "/explode":
			x,y,z=string_to_position(string, entity)
			r=int(string.split()[4])
			chunk.explode(x,y,z,r)
		else:
			show_text("Unknown or incomplete command: "+string, [255,85,85,255])
			logger.set_environment("Main")
			logger.info("[COMMAND] Unknown or incomplete command: "+string)
			logger.set_environment("Client")
	except Exception as e:
		show_text("Unknown or incomplete command: "+string, [255,85,85,255])
		logger.set_environment("Main")
		logger.info("[COMMAND] Unknown or incomplete command: "+string+" | Error: "+str(traceback.format_exc()))
		logger.set_environment("Client")
