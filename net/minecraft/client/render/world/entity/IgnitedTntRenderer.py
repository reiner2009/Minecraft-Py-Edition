from net.minecraft.client import*
from net.minecraft.client.render.world.block.BlockRenderer import block_atlas, place_block


def renderIgnitedTnt(x, y, z, c):
	glBindTexture(GL_TEXTURE_2D, block_atlas)
	t=(c/60) % 0.5
	if t < 0.25:
		glColor3f(1,1,1)
		place_block("tnt",x,y,z, "", True)
	else:
		glDisable(GL_BLEND)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_BLEND)
		glColor3f(0.1,0.1,0.1)
		place_block("tnt",x,y,z, "", True)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
