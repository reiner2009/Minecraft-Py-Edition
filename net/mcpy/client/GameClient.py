from net.mcpy.client.TextureLoader import load_texture

attributes={}
textures={}
block_atlas=None
crosshair_texture=None

def init():
	global textures, block_atlas, crosshair_texture
	block_atlas=load_texture("assets/minecraft/textures/block/atlas.png")
	hud_atlas=load_texture("assets/minecraft/textures/gui/sprites/hud/atlas.png")
	textures={"block_atlas":block_atlas, "hud_atlas":hud_atlas}

def textures():
	global textures
	return textures
