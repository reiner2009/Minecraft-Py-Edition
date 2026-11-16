from net.mcpy.client.TextureLoader import load_texture


attributes={}
textures={}
block_atlas=None

def init():
	global textures, block_atlas
	block_atlas=load_texture("assets/minecraft/textures/block/atlas.png")
	textures={"block_atlas":block_atlas}

def textures():
	global textures
	return textures
