from net.minecraft.world.chunk.Chunk import *
import net.minecraft.util.logger.Logger as logger
import net.minecraft.world.chunk.Chunk as chunk
import net.minecraft.entity.player.Playername as Playername
import net.minecraft.entity.Entities as Entities
import net.minecraft.world.EntityList as EntityList

temporary_texts=[]
texts=[]
LINE_HIGHT=24
CHAT_BASE_Y=100

def irange(o,t):
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

def split_text(text, max_len=53):
    words = text.split()
    parts = []
    current = ""
    for word in words:
        if len(word) > max_len:
            if current:
                parts.append(current)
                current = ""
            for i in range(0, len(word), max_len):
                parts.append(word[i:i+max_len])
            continue
        if len(current) + len(word) + (1 if current else 0) <= max_len:
            if current:
                current += " "
            current += word
        else:
            parts.append(current)
            current = word
    if current:
        parts.append(current)
    return parts

def show_text(msg, color, lifetime=10000):
	msg=str(msg)
	msgs=split_text(msg)
	for i in msgs:
		temporary_texts.insert(0,{
			"text":i,
			"spawn_time":pygame.time.get_ticks(),
			"life_time":lifetime,
			"color":color
		})
		texts.insert(0, {
			"text":i,
			"color":color
		})
	if len(temporary_texts)>10:
		temporary_texts.pop()
def render_temporary_texts():
	current_time=pygame.time.get_ticks()
	hud.render_chat_background(98,len(temporary_texts)*24)
	for i, t in enumerate(temporary_texts[:]):
		if current_time-t["spawn_time"]>t["life_time"]:
			temporary_texts.remove(t)
			continue
		y=CHAT_BASE_Y+i*LINE_HIGHT
		text.render_text(t["text"], 15, y, 20,20,t["color"])

def render_texts():
	hud.render_chat_background(98,len(texts)*24)
	for i, t in enumerate(texts[:]):
		y=CHAT_BASE_Y+i*LINE_HIGHT
		text.render_text(t["text"], 15, y, 20,20,t["color"])

def assume_command(string, entity, chunklist):
	try:
		if string.split()[0]=="/setblock":
			set_block(*string_to_position(string, entity), string.split()[4])
			rebuild_chunks(chunklist)
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
			rebuild_chunks(chunklist)
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
			rebuild_chunks(chunklist)
			show_text("World successfully reset ", [255, 255, 255, 255])
			logger.set_environment("Main")
			logger.info("[COMMAND] World successfully reset")
		elif string.split()[0]=="/summon":
			x,y,z=string_to_position(string, entity)
			entityName=string.split()[4]
			entity=Entities.entites[entityName](True)
			entity.spawn(x,y,z)
			try:
				entity.setName(string.split()[5])
			except:
				entity.setName("Steve")
			try:
				entity.setSkin(string.split()[6])
			except:
				entity.setSkin("assets/minecraft/textures/entity/player/steve.png")
			entity.set_thirt_person_perspective()
			EntityList.entities.append(entity)
			logger.info(f"[COMMAND] Added {entityName} successfully at {string_to_position(string, entity)}")
			show_text(f"Added {entityName} successfully at {string_to_position(string, entity)}", [255, 255, 255, 255])
		elif string.split()[0]=="/time":
			t=float(string.split()[1])
			set_tick(t)
		else:
			show_text("Unknown or incomplete command: "+string, [255,85,85,255])
			logger.set_environment("Main")
			logger.info("[COMMAND] Unknown or incomplete command: "+string)
			logger.set_environment("Client")
	except Exception as e:
		show_text("Unknown or incomplete command: "+string, [255,85,85,255])
		logger.set_environment("Main")
		logger.info("[COMMAND] Unknown or incomplete command: "+string+" | Error: "+str(e))
		logger.set_environment("Client")

def rebuild_chunks(chunklist):
	glDeleteLists(chunklist, 1)
	chunklist=build_chunk_display_list()