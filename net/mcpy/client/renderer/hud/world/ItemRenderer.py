from net.mcpy.client.renderer.ShaderCompiler import ShaderCompiler
from net.mcpy.client.renderer.world.block.Models import models, uv, width, height
import net.mcpy.client.GameClient as GameClient
from OpenGL.GL import *
import numpy as np
import ctypes

hud_shader = None
position = None
aUv = None

def init():
    global hud_shader, position, aUv
    hud_shader = ShaderCompiler(
        "assets/minecraft/shader/hud.vert",
        "assets/minecraft/shader/hud.frag"
    ).createShaderProgram()
    position = glGetAttribLocation(hud_shader, "position")
    aUv = glGetAttribLocation(hud_shader, "uv")


def getVertices(hotbar):
	vertex_array=[]
	hotbar_item_pos=-1
	w_width=GameClient.attributes["resolution"][0]
	w_height=GameClient.attributes["resolution"][1]
	aspect = w_height / w_width
	for block in hotbar:
		hotbar_item_pos+=1
		size_y = 0.06
		size_x = size_y * (16 / 16)
		step_x = (0.1 + 0.009) * (24 / 23)
		x0 = -size_x * aspect - (step_x * 4) + (step_x * hotbar_item_pos)
		y0 = -size_y - 1 + size_y + 0.009*4
		x1 = size_x * aspect - (step_x * 4) + (step_x * hotbar_item_pos)
		y1 = size_y - 1 + size_y + 0.009*4
		model=models[block.id.getAsString()+block.getState()]
		texture=model["textures"][3]
		u0=uv[texture][0]/width
		u1=(uv[texture][0]+1)/width
		v0=uv[texture][1]/height
		v1=(uv[texture][1]+1)/height
		for i in [
			x0, y1, u0, v0,
			x0, y0, u0, v1,
			x1, y0, u1, v1,
			x0, y1, u0, v0,
			x1, y0, u1, v1,
			x1, y1, u1, v0,
		]:
			vertex_array.append(i)
	return vertex_array


class ItemRenderer:
    def __init__(self, hotbar):
        self.vertex_array = getVertices(hotbar)
        self.vertices = np.array(self.vertex_array, dtype=np.float32)
        self.vertex_count = len(self.vertices) // 4
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_DYNAMIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
    def render(self):
        previous_shader = glGetIntegerv(GL_CURRENT_PROGRAM)
        glUseProgram(hud_shader)
        glActiveTexture(GL_TEXTURE0)
        loc_texture = glGetUniformLocation(hud_shader, "texture")
        glUniform1i(loc_texture, 0)
        self.bind()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)
        glUseProgram(previous_shader)
    def update(self, hotbar):
        self.vertex_array = getVertices(hotbar)
        self.new_vertices = np.array(self.vertex_array, dtype=np.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.new_vertices, GL_DYNAMIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        self.vertices=self.new_vertices
        self.new_vertices=[]
    def bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glVertexAttribPointer(position, 2, GL_FLOAT, GL_FALSE,16, ctypes.c_void_p(0))
        glEnableVertexAttribArray(position)
        glVertexAttribPointer(aUv, 2, GL_FLOAT, GL_FALSE,16, ctypes.c_void_p(8))
        glEnableVertexAttribArray(aUv)
