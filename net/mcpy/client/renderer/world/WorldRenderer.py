from OpenGL.GL import*
import glm
import net.mcpy.client.renderer.world.level.LevelRenderer as LevelRendererModule
from net.mcpy.client.renderer.world.level.LevelRenderer import LevelRenderer
import net.mcpy.client.renderer.world.BlockOutlinesRenderer as BlockOutlinesRendererModule
from net.mcpy.client.renderer.world.BlockOutlinesRenderer import BlockOutlinesRenderer
import net.mcpy.client.renderer.hud.world.HudRenderer as HudRendererModule
from net.mcpy.client.renderer.hud.world.HudRenderer import HUDRenderer
import net.mcpy.client.GameClient as GameClient

level_renderer=None

model=glm.mat4(1.0)
view=glm.mat4(1.0)
projection=glm.mat4(1.0)

block_outline_renderer=None
hud_renderer=None

def init():
	global level_renderer, projection,  block_outline_renderer, hud_renderer
	width=GameClient.attributes["resolution"][0]
	height=GameClient.attributes["resolution"][1]
	LevelRendererModule.init()
	level_renderer=LevelRenderer()
	projection=glm.perspective(glm.radians(85.0), width/height, 0.1, 1000.0)
	BlockOutlinesRendererModule.init()
	block_outline_renderer=BlockOutlinesRenderer()
	HudRendererModule.init()
	hud_renderer=HUDRenderer()

def render():
	global model, view, projection
	updateView()
	glBindTexture(GL_TEXTURE_2D, GameClient.textures["block_atlas"])
	level_renderer.render(model, view, projection)
	block_outline_renderer.render(model, view, projection)
	glBindTexture(GL_TEXTURE_2D, GameClient.textures["crosshair_texture"])
	hud_renderer.render()


def updateVertices():
	level_renderer.updateVertices()

def updateView():
	global model, view, direction, camera_pos
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
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
