from net.minecraft.world.block.Block import*
import net.minecraft.util.gui.Hud as hud
import net.minecraft.text.Text as text
import pickle
import net.minecraft.resources.DataLocation as DataLocation
import net.minecraft.world.DefaultMap as default_map

dirt_wallpaper_texture=load_texture("assets/minecraft/textures/gui/title/background/dirt_wallpaper.webp")

def get_block_in_chunk(x,y,z):
	return x % 8, y % 8, z % 8

def build_chunk_display_list(light=1):
	dl = glGenLists(1)
	glNewList(dl, GL_COMPILE)
	build_chunk([light,light,light,1])
	pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
	glEndList()
	return dl

def render_chunk():
	global chunk
	try:
		chunk.clear()
		base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
		world = os.path.join(base_path, "world")
		full_path = os.path.join(world, "chunks.dat")
		with open(full_path, "rb") as f:
			_chunk=pickle.load(f)
		pygame.mouse.set_cursor(SYSTEM_CURSOR_WAIT)
		setup_ortho()
		hud.render_wallpaper(dirt_wallpaper_texture)
		text.render_text("Loading terrian.,,", width / 2 - 67, height - height / 1152 * 200, 15, 15, [255, 255, 255, 255])
		pygame.display.flip()
		clock.tick(60)
		logger.info("Loading terrian")
		for (x,y,z), block_name in _chunk.items():
			set_block(x,y,z, block_name)
	except:
		logger.set_environment("Main")
		logger.info("No existing world data, creating new world")
		logger.set_environment("Client")
		pygame.mouse.set_cursor(SYSTEM_CURSOR_WAIT)
		setup_ortho()
		hud.render_wallpaper(dirt_wallpaper_texture)
		text.render_text("Loading terrian.,,", width / 2 - 67, height - height / 1152 * 200, 15, 15, [255, 255, 255, 255])
		pygame.display.flip()
		clock.tick(60)
		logger.info("Loading terrian")
		chunk.clear()
		chunk_= default_map.map
		for (x,y,z), block_name in chunk_.items():
			set_block(x,y,z,block_name)

def set_block(x,y,z,name):
	global blocks
	if not name in blocks:
		name="air"
	if name != "air":
		global chunk
		chunk[(x,y,z)]=name
	else:
		chunk.pop((x,y,z), None)

def build_chunk(color):
	global chunk
	glEnable(GL_CULL_FACE)
	glDepthMask(GL_TRUE)
	glDisable(GL_BLEND)
	for (x, y, z), block_name in chunk.items():
		if block_name not in translucent_blocks and block_name not in cutout_blocks:
			place_block(block_name, x, y, z, color)
	glEnable(GL_ALPHA_TEST)
	glAlphaFunc(GL_GREATER, 0.5)
	for (x, y, z), block_name in chunk.items():
		if block_name in cutout_blocks:
			place_block(block_name, x, y, z, color)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	for (x, y, z), block_name in chunk.items():
		if block_name in translucent_blocks:
			place_block(block_name, x, y, z, color)
	glDisable(GL_ALPHA_TEST)
	glDepthMask(GL_TRUE)

def save_world():
	global chunk
	base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
	world = os.path.join(base_path, "world")
	full_path = os.path.join(world, "chunks.dat")
	try:
		with open(full_path, "wb") as f:
			pickle.dump(chunk, f)
	except:
		os.mkdir(world)
		with open(full_path, "wb") as f:
			pickle.dump(chunk, f)

def rebuild_chunks():
	global chunklist
	glDeleteLists(chunklist, 1)
	chunklist=build_chunk_display_list()