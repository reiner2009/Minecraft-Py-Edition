from OpenGL.GL import *
from PIL import Image
import net.mcpy.resources.FileLoader as FileLoader

def load_texture(path):
	image = Image.open(FileLoader.getFromModOrFrozen(path)).convert("RGBA")
	image_data = image.tobytes()
	width, height = image.size
	tex_id = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, tex_id)
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,width, height, 0,GL_RGBA, GL_UNSIGNED_BYTE, image_data)
	return tex_id
