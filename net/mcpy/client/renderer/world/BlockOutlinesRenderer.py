from net.mcpy.client.renderer.ShaderCompiler import ShaderCompiler
import net.mcpy.client.GameClient as GameClient
from OpenGL.GL import*
import numpy as np
import ctypes
import glm

line_shader=None
position=None

def init():
	global line_shader, position
	line_shader=ShaderCompiler(
		"assets/minecraft/shader/line.vert",
		"assets/minecraft/shader/line.frag"
	).createShaderProgram()
	position=glGetAttribLocation(line_shader, "position")
	
def getVertices(vx,vy,vz):
	x=round(vx)
	y=round(vy)
	z=round(vz)
	return[
		0+x,0+y,0+z,
		1+x,0+y,0+z,
		1+x,0+y,0+z,
		1+x,0+y,1+z,
		1+x,0+y,1+z,
		0+x,0+y,1+z,
		0+x,0+y,1+z,
		0+x,0+y,0+z,
		0+x,1+y,0+z,
		1+x,1+y,0+z,
		1+x,1+y,0+z,
		1+x,1+y,1+z,
		1+x,1+y,1+z,
		0+x,1+y,1+z,
		0+x,1+y,1+z,
		0+x,1+y,0+z,
		0+x,0+y,0+z,
		0+x,1+y,0+z,
		1+x,0+y,0+z,
		1+x,1+y,0+z,
		1+x,0+y,1+z,
		1+x,1+y,1+z,
		0+x,0+y,1+z,
		0+x,1+y,1+z
	]

class BlockOutlinesRenderer:
	def __init__(self):
		self.vertex_array=getVertices(*GameClient.attributes["local_player"].getTrackedPos())
		self.vertices=np.array(self.vertex_array, dtype=np.float32)
		self.vertex_count=len(self.vertices) // 3
		self.vbo=glGenBuffers(1)
		glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
		glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_DYNAMIC_DRAW)
		glBindBuffer(GL_ARRAY_BUFFER, 0)
	def render(self, model, view, projection):
		previous_shader=glGetIntegerv(GL_CURRENT_PROGRAM)
		glUseProgram(line_shader)
		loc_model=glGetUniformLocation(line_shader, "model")
		loc_view=glGetUniformLocation(line_shader, "view")
		loc_projection=glGetUniformLocation(line_shader, "projection")
		glUniformMatrix4fv(loc_model, 1, GL_FALSE, glm.value_ptr(model))
		glUniformMatrix4fv(loc_view, 1, GL_FALSE, glm.value_ptr(view))
		glUniformMatrix4fv(loc_projection, 1, GL_FALSE, glm.value_ptr(projection))
		self.bind()
		glDrawArrays(GL_LINES, 0, self.vertex_count)
		self.updateVbo()
		glUseProgram(previous_shader)
	def updateVbo(self):
		self.vertex_array=getVertices(*GameClient.attributes["local_player"].getTrackedPos())
		self.new_vertices=np.array(self.vertex_array, dtype=np.float32)
		glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
		glBufferData(GL_ARRAY_BUFFER, self.new_vertices.nbytes, self.new_vertices, GL_DYNAMIC_DRAW)
		self.vertices=self.new_vertices
		self.vertex_count=len(self.new_vertices)//3
		glBindBuffer(GL_ARRAY_BUFFER, 0)
	def bind(self):
		glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
		glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 3*4, ctypes.c_void_p(0))
		glEnableVertexAttribArray(position)
