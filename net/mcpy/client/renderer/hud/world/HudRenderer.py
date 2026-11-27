from net.mcpy.client.renderer.ShaderCompiler import ShaderCompiler
import net.mcpy.client.GameClient as GameClient
from OpenGL.GL import *
import numpy as np
import ctypes

hud_shader = None
position = None
uv = None

def init():
    global hud_shader, position, uv
    hud_shader = ShaderCompiler(
        "assets/minecraft/shader/hud.vert",
        "assets/minecraft/shader/hud.frag"
    ).createShaderProgram()
    position = glGetAttribLocation(hud_shader, "position")
    uv = glGetAttribLocation(hud_shader, "uv")


def getVertices():
    vertex_array=[]
    width=GameClient.attributes["resolution"][0]
    height=GameClient.attributes["resolution"][1]
    aspect = height / width
    size=0.05
    x0=-size*aspect
    y0=-size
    x1=size*aspect
    y1=size
    u0=0
    v0=0
    u1=15/182
    v1=15/45
    for i in  [
			x0,y1,u0,v0,
			x0,y0,u0,v1,
			x1,y0,u1,v1,
			x0,y1,u0,v0,
			x1,y0,u1,v1,
			x1,y1,u1,v0,
	]:
        vertex_array.append(i)
    size_y = 0.1
    size_x = size_y * (182 / 22)
    x0 = -size_x * aspect
    y0 = -size_y - 1 + size_y
    x1 = size_x * aspect
    y1 = size_y - 1 + size_y
    u0 = 0
    v0 = 23/45
    u1 = 1
    v1 = 1
    for i in [
        x0, y1, u0, v0,
        x0, y0, u0, v1,
        x1, y0, u1, v1,
        x0, y1, u0, v0,
        x1, y0, u1, v1,
        x1, y1, u1, v0,
    ]:
        vertex_array.append(i)
    size_y = 0.1
    size_x = size_y * (24 / 23)
    x0 = -size_x * aspect
    y0 = -size_y - 1 + size_y
    x1 = size_x * aspect
    y1 = size_y - 1 + size_y
    u0 = 15/182
    v0 = 0
    u1 = 39/182
    v1 = 23/45
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


class HUDRenderer:
    def __init__(self):
        self.vertex_array = getVertices()
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
    def bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glVertexAttribPointer(position, 2, GL_FLOAT, GL_FALSE,16, ctypes.c_void_p(0))
        glEnableVertexAttribArray(position)
        glVertexAttribPointer(uv, 2, GL_FLOAT, GL_FALSE,16, ctypes.c_void_p(8))
        glEnableVertexAttribArray(uv)
