from net.minecraft.world.EntityList import entities
from net.minecraft.client.render.world.block.BlockRenderer import*
import net.minecraft.util.gui.Hud as hud
import net.minecraft.text.Text as text
import pickle
import net.minecraft.resources.DataLocation as DataLocation
from opensimplex import OpenSimplex
import random

dark_menu_texture=load_texture("assets/minecraft/textures/gui/title/background/dark_menu.png")

def create_random_chunk(_x_=0, _z_=0, seed=0):
	noise=OpenSimplex(seed=seed)
	c={}
	tree_map = []
	for x in range(50):
		for z in range(50):
			c[(x,-1,z)]="stone"
	for x_ in range(50):
		for z_ in range(50):
			x=x_+_x_*16
			z=z_+_z_*16
			value=noise.noise2(x * 0.05, z * 0.05)*10+6
			ay=round(value)
			for y in range(ay):
				if (x,y,z) not in c:
					c[(x,y,z)]="dirt"
			for y in range(ay):
				if y==ay-1:
					c[(x,y,z)]="grass_block"
	for x in range(50):
		for z in range(50):
			tree_wight=random.randint(0,100)
			if tree_wight<1:
				tree_map.append((x,noise.noise2(x * 0.05, z * 0.05)*10+6, z))
	with open("data/minecraft/worldgen/feature/tree.dat", "rb") as f:
		tree=pickle.load(f)
	for i in tree_map:
		for pos, block in tree.items():
			c[(round(pos[0]+i[0]),round(pos[1]+i[1]),round(pos[2]+i[2]))]=block
	for player in entities:
		player.spawn(25,round(noise.noise2(25 * 0.05, 25 * 0.05)*10+7), 25)
	return c

def build_chunk_display_list():
	dl = glGenLists(1)
	glNewList(dl, GL_COMPILE)
	glBindTexture(GL_TEXTURE_2D, block_atlas)
	build_chunk()
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
		hud.render_wallpaper(dark_menu_texture)
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
		create_new_world()


def create_new_world():
	global chunk
	pygame.mouse.set_cursor(SYSTEM_CURSOR_WAIT)
	setup_ortho()
	hud.render_wallpaper(dark_menu_texture)
	text.render_text("Loading terrian.,,", width / 2 - 67, height - height / 1152 * 200, 15, 15, [255, 255, 255, 255])
	pygame.display.flip()
	clock.tick(60)
	logger.info("Loading terrian")
	chunk.clear()
	chunk_ = create_random_chunk(seed=random.randint(0,100))
	for (x, y, z), block_name in chunk_.items():
		set_block(x, y, z, block_name)

def set_block(x,y,z,name):
	global blocks
	if not name in blocks:
		name="air"
	if name != "air":
		global chunk
		chunk[(x,y,z)]=name
	else:
		chunk.pop((x,y,z), None)

def build_chunk():
	glEnable(GL_CULL_FACE)
	glDepthMask(GL_TRUE)
	glDisable(GL_BLEND)
	for (x, y, z), block_name in chunk.items():
		if block_name not in translucent_blocks and block_name not in cutout_blocks:
			place_block(block_name, x, y, z)
	glEnable(GL_ALPHA_TEST)
	glAlphaFunc(GL_GREATER, 0.5)
	for (x, y, z), block_name in chunk.items():
		if block_name in cutout_blocks:
			place_block(block_name, x, y, z)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	for (x, y, z), block_name in chunk.items():
		if block_name in translucent_blocks:
			place_block(block_name, x, y, z)
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