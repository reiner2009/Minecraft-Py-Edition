from net.minecraft.client.Client import*
from net.minecraft.client.render.world.block.BlockRenderer import block_atlas, place_block


def renderFallingBlock(x, y, z, name):
	glBindTexture(GL_TEXTURE_2D, block_atlas)
	place_block(name,x,y,z, "", True)
