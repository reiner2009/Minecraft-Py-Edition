from net.minecraft.client.render.world.block.BlockRenderer import*
import net.minecraft.client.render.gui.Hud as hud
import net.minecraft.client.render.Text as text
import pickle
import net.minecraft.resources.DataLocation as DataLocation
from opensimplex import OpenSimplex
import random
import gzip
import math
import net.minecraft.world.Features as features
from net.minecraft.world.block.Blocks import registries
import net.minecraft.client.Sounds as Sounds
from net.minecraft.world.EntityList import entity_chunk
import net.minecraft.client.render.world.SkyRenderer as SkyRenderer
import net.minecraft.client.render.world.ItemRenderer as ItemRenderer
import net.minecraft.chat.Chat as Chat

dark_menu_texture=load_texture("assets/minecraft/textures/gui/title/background/dark_menu.png")
base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
pack = os.path.join(base_path, "datapacks")
os.makedirs(pack, exist_ok=True)
chunklist=None

def create_random_chunk(seed=0):
	tree_percent_map=features.get_feature_list("tree")
	noise_settings=json.load(open(DataLocation.get_resource_path("data/minecraft/worldgen/noise_settings/overworld.json")))
	noise=OpenSimplex(seed=seed)
	c={}
	tree_map = []
	for x in range(noise_settings["world_scale"]):
		for z in range(noise_settings["world_scale"]):
			value=noise.noise2(x * noise_settings["x"], z * noise_settings["z"])*noise_settings["hilly_intensity"]+noise_settings["terrian_height"]
			ay=round(value)
			for y in range(ay):
				if (x,y,z) not in c:
					c[(x,y,z)]="dirt"
			for y in range(ay):
				if y==ay-1:
					c[(x,y,z)]="grass_block"
	for x in range(noise_settings["world_scale"]):
		for z in range(noise_settings["world_scale"]):
			tree_wight=random.randint(0,100)
			if tree_wight==0:
				tree_map.append((x, noise.noise2(x*noise_settings["x"], z * noise_settings["z"])*noise_settings["hilly_intensity"]+noise_settings["terrian_height"], z))
	for i in tree_map:
		feature=random.choices(list(tree_percent_map.keys()), weights=tree_percent_map.values())[0]
		with gzip.open(DataLocation.get_resource_path("data/minecraft/worldgen/feature/tree/" + feature + ".dat"), "rb") as file:
			tree=pickle.load(file)
		for pos, block in tree.items():
			c[(round(pos[0]+i[0]),round(pos[1]+i[1]),round(pos[2]+i[2]))]=block.getName()
	for player in entity_chunk:
		player.spawn(25,round(noise.noise2(25 * noise_settings["x"], 25 * noise_settings["z"])*noise_settings["hilly_intensity"]+noise_settings["terrian_height"]+1), 25)
	return c

def build_chunk_display_list():
	dl = glGenLists(1)
	glNewList(dl, GL_COMPILE)
	glBindTexture(GL_TEXTURE_2D, block_atlas)
	for (x,y,z), block in chunk.items():
		name=block.getName()
		if get_block(x, y, z)!="air":
			if get_block(x, y, z) not in translucent_blocks and get_block(x, y, z) not in cutout_blocks:
				glDisable(GL_BLEND)
				place_block(name, x, y, z, get_block_data(x,y,z).getProperty())
			if get_block(x, y, z) in cutout_blocks:
				glDisable(GL_BLEND)
				glEnable(GL_ALPHA_TEST)
				glAlphaFunc(GL_GREATER, 0.5)
				place_block(name, x, y, z, get_block_data(x,y,z).getProperty())
			if get_block(x, y, z) in translucent_blocks:
				glEnable(GL_BLEND)
				glEnable(GL_ALPHA_TEST)
				glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
				place_block(name, x, y, z, get_block_data(x,y,z).getProperty())
			glDepthMask(GL_TRUE)
	pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
	glEndList()
	ItemRenderer.build_hotbar_items()
	ItemRenderer.buildInventory()
	SkyRenderer.build()
	return dl

def render_chunk():
	global chunk
	try:
		chunk.clear()
		base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
		world = os.path.join(base_path, "world")
		full_path = os.path.join(world, "chunks.dat")
		with gzip.open(full_path, "rb") as f:
			_chunk=pickle.load(f)
		pygame.mouse.set_cursor(SYSTEM_CURSOR_WAIT)
		setup_ortho()
		hud.render_wallpaper(dark_menu_texture)
		text.render_text("Loading terrian...", width / 2 - 67, height - height / 1152 * 200, 15, 15, [255, 255, 255, 255])
		pygame.display.flip()
		clock.tick(60)
		logger.info("Loading terrian")
		for (x,y,z), block in _chunk.items():
			chunk[(x,y,z)]=block
		load_chunks()
	except:
		logger.set_environment("Main")
		logger.info("No existing world data, creating new world")
		logger.set_environment("Client")
		create_new_world()
		load_chunks()

def create_new_world():
	global chunk
	pygame.mouse.set_cursor(SYSTEM_CURSOR_WAIT)
	setup_ortho()
	hud.render_wallpaper(dark_menu_texture)
	text.render_text("Loading terrian...", width / 2 - 67, height - height / 1152 * 200, 15, 15, [255, 255, 255, 255])
	pygame.display.flip()
	clock.tick(60)
	logger.info("Loading terrian")
	chunk.clear()
	chunk_ = create_random_chunk(seed=random.randint(0,100))
	for (x, y, z), block in chunk_.items():
		set_block(x, y, z, block)
	reload_chunks()

def updateNigbours(x,y,z):
	nighbours=[(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]
	for X,Y,Z in nighbours:
		get_block_data(X,Y,Z).update()

def set_block(x,y,z,name):
	global blocks
	if not name in blocks:
		name="air"
	if name != "air":
		global chunk
		tc=registries[name](name)
		tc.setPos(x,y,z)
		chunk[(x,y,z)]=tc
	else:
		chunk.pop((x,y,z), None)
	updateNigbours(x,y,z)

def explode(world_x, world_y, world_z, radius, v=489):
	Sounds.play_block_sound("explode", v)
	for yaw in range(36):
		for pitch in range(36):
			for ran in range(radius):
				tx=round(world_x+(math.sin(math.radians(yaw*10))*math.cos(math.radians(pitch*10)))*ran)
				ty=round(world_y-(math.sin(math.radians(pitch*10)))*ran)
				tz=round(world_z-(math.cos(math.radians(yaw*10))*math.cos(math.radians(pitch*10)))*ran)
				get_block_data(tx,ty,tz).onExplode(v)
	reload_chunks()

def build_chunk():
	glEnable(GL_CULL_FACE)
	for (x, y, z), block in chunk.items():
		place_block(block.getName(), x, y, z, block.getProperty())

def save_world():
	global chunk
	base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
	world = os.path.join(base_path, "world")
	full_path = os.path.join(world, "chunks.dat")
	try:
		pygame.mouse.set_cursor(SYSTEM_CURSOR_WAIT)
		setup_ortho()
		hud.render_wallpaper(dark_menu_texture)
		text.render_text("Saving world...", width / 2 - 67, height - height / 1152 * 200, 15, 15, [255, 255, 255, 255])
		pygame.display.flip()
		clock.tick(60)
		with gzip.open(full_path, "wb", compresslevel=9) as f:
			pickle.dump(chunk, f)
	except:
		pygame.mouse.set_cursor(SYSTEM_CURSOR_WAIT)
		setup_ortho()
		hud.render_wallpaper(dark_menu_texture)
		text.render_text("Saving world...", width / 2 - 67, height - height / 1152 * 200, 15, 15, [255, 255, 255, 255])
		pygame.display.flip()
		clock.tick(60)
		os.mkdir(world)
		with gzip.open(full_path, "wb", compresslevel=9) as f:
			pickle.dump(chunk, f)

def reload_chunks():
	global chunklist, global_vertices
	glDeleteLists(chunklist, 1)
	build_chunk()
	chunklist=build_chunk_display_list()

def load_chunks():
	global chunklist
	build_chunk()
	chunklist=build_chunk_display_list()

def getChunkList():
	global chunklist
	if chunklist==None:
		return None
	else:
		return chunklist

def unload_chunks():
	global chunklist
	try:
		glDeleteLists(chunklist, 1)
	except:
		pass
	chunklist=None
	SkyRenderer.unload()
