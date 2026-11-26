from OpenGL.GL import *
import net.mcpy.resources.FileLoader as FileLoader

class ShaderError(RuntimeError):
	def __init__(self, msg):
		pass

class ShaderCompiler:
	def __init__(self, vertex_path, fragment_path):
		self.vertex_path=FileLoader.getFromModOrFrozen(vertex_path)
		self.fragment_path=FileLoader.getFromModOrFrozen(fragment_path)
	def loadShader(self, path, shader_type):
		with open(path, "r") as file:
			source = file.read()
		shader = glCreateShader(shader_type)
		glShaderSource(shader, source)
		glCompileShader(shader)
		if not glGetShaderiv(shader, GL_COMPILE_STATUS):
			error = glGetShaderInfoLog(shader)
			raise ShaderError(str(error))
		return shader
	def createShaderProgram(self):
		self.vertex = self.loadShader(self.vertex_path, GL_VERTEX_SHADER)
		self.fragment = self.loadShader(self.fragment_path, GL_FRAGMENT_SHADER)
		self.program = glCreateProgram()
		glAttachShader(self.program, self.vertex)
		glAttachShader(self.program, self.fragment)
		glLinkProgram(self.program)
		if not glGetProgramiv(self.program, GL_LINK_STATUS):
			error = glGetProgramInfoLog(self.program)
			raise ShaderError(str(error))
		glDeleteShader(self.vertex)
		glDeleteShader(self.fragment)
		return self.program
