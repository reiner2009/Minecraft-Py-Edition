from net.mcpy.client.renderer.ShaderCompiler import ShaderCompiler
import net.mcpy.client.GameClient as GameClient
import net.mcpy.client.renderer.world.block.BlockRenderer as BlockRenderer
import net.mcpy.resources.FileLoader as FileLoader
from net.mcpy.game.Minecraft import level
from OpenGL.GL import*
import numpy as np
import ctypes
import glm
import json
import threading

width=None
height=None
position=0
model=glm.mat4(1.0)
view=glm.mat4(1.0)
projection=glm.mat4(1.0)
direction=glm.vec3()
block_shader=None

render_data=json.load(open(FileLoader.getFromModOrFrozen("assets/minecraft/render/render_data.json")))

def getRenderData(block):
	block_id=block.id.getAsString()
	if block_id in render_data["cutout"]:
		return "cutout"
	if block_id in render_data["translucent"]:
		return "translucent"
	else:
		return "solide"

def init():
	global block_shader, width, height, projection, direction, position
	block_shader=ShaderCompiler(
		"assets/minecraft/shader/block.vert",
		"assets/minecraft/shader/block.frag"
	).createShaderProgram()
	width=GameClient.attributes["resolution"][0]
	height=GameClient.attributes["resolution"][1]
	projection=glm.perspective(glm.radians(85.0), width/height, 0.1, 1000.0)
	direction=glm.normalize(glm.vec3(glm.inverse(view)[2]) * -1)
	position=glGetAttribLocation(block_shader, "position")

def updateView():
	global model, view, direction, dirty
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glUseProgram(block_shader)
	camera_x, camera_y, camera_z=GameClient.attributes["local_player"].getPos()
	pitch=glm.radians(GameClient.attributes["local_player"].pitch)
	yaw=glm.radians(GameClient.attributes["local_player"].yaw)
	direction = glm.normalize(glm.vec3(
		glm.cos(pitch)*glm.sin(yaw),
		glm.sin(pitch),
		glm.cos(pitch)*glm.cos(yaw)
	))
	camera_pos=glm.vec3(camera_x, camera_y, camera_z)
	view=glm.lookAt(camera_pos, camera_pos+direction, glm.vec3(0,1,0))


class ChunkRenderer:
	def __init__(self, block_render_type, chunk):
		self.dirty=False
		self.vbodirty=False
		self.chunk=chunk
		self.mesh_lock=threading.Lock()
		self.block_render_type=block_render_type
		self.vertex_array=[]
		self.updateVertices(False)
		self.vertices=np.array(self.vertex_array, dtype=np.float32)
		self.vertex_count=len(self.vertices) // 8
		self.vbo=glGenBuffers(1)
		self.texCoord=glGetAttribLocation(block_shader, "texCoord")
		self.normal=glGetAttribLocation(block_shader, "aNormal")
		glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
		glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_DYNAMIC_DRAW)
		glBindBuffer(GL_ARRAY_BUFFER, 0)
	def render(self):
		glActiveTexture(GL_TEXTURE0)
		loc_model=glGetUniformLocation(block_shader, "model")
		loc_view=glGetUniformLocation(block_shader, "view")
		loc_projection=glGetUniformLocation(block_shader, "projection")
		loc_texture=glGetUniformLocation(block_shader, "texture")
		loc_cutout=glGetUniformLocation(block_shader, "cutout")
		glUniform1i(loc_cutout, int(self.block_render_type=="cutout"))
		glUniform1i(loc_texture, 0)
		glUniformMatrix4fv(loc_model, 1, GL_FALSE, glm.value_ptr(model))
		glUniformMatrix4fv(loc_view, 1, GL_FALSE, glm.value_ptr(view))
		glUniformMatrix4fv(loc_projection, 1, GL_FALSE, glm.value_ptr(projection))
		self.bind()
		glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)
		if self.vbodirty:
			self.updateVbo()
			self.vbodirty=False
	def updateVertices(self, set_dirty=True):
		global level
		with self.mesh_lock:
			self.vertex_array=[]
			with self.chunk.lock:
				for (x,y,z),block in self.chunk.blocks.items():
					if getRenderData(block)==self.block_render_type:
						for num in BlockRenderer.getVertices(self.chunk.x * 8 + x, y, self.chunk.z * 8 + z, block, level):
							self.vertex_array.append(num)
			self.chunk.dirty=False
			if set_dirty:
				self.vbodirty=True
	def updateVbo(self):
		with self.mesh_lock:
			self.new_vertices=np.array(self.vertex_array, dtype=np.float32)
		glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
		glBufferData(GL_ARRAY_BUFFER, self.new_vertices.nbytes, self.new_vertices, GL_DYNAMIC_DRAW)
		self.vertices=self.new_vertices
		self.vertex_count=len(self.new_vertices)//8
		glBindBuffer(GL_ARRAY_BUFFER, 0)
	def bind(self):
		glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
		glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
		glEnableVertexAttribArray(position)
		glVertexAttribPointer(self.texCoord, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
		glEnableVertexAttribArray(self.texCoord)
		glVertexAttribPointer(self.normal, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(20))
		glEnableVertexAttribArray(self.normal)
