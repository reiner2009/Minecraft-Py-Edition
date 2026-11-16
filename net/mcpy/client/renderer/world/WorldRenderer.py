from OpenGL.GL import*
import net.mcpy.client.renderer.world.level.LevelRenderer as LevelRendererModule
from net.mcpy.client.renderer.world.level.LevelRenderer import LevelRenderer

level_renderer=None

def init():
	global level_renderer
	LevelRendererModule.init()
	level_renderer=LevelRenderer()

def render():
	LevelRendererModule.updateView()
	level_renderer.render()

def updateVertices():
	level_renderer.updateVertices()
