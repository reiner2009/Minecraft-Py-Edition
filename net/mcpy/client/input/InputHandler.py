import glfw
import glm
import net.mcpy.client.GameClient as GameClient
import net.mcpy.game.GameTickThread as GameTickThread
import net.mcpy.game.Minecraft as Minecraft
import net.mcpy.world.block.Blocks as Blocks
import net.mcpy.client.renderer.world.WorldRenderer as WorldRenderer
from net.mcpy.game.Hotbar import hotbar

def sin(i):
	return glm.sin(glm.radians(i))

def cos(i):
	return glm.cos(glm.radians(i))

w_pressed=False
a_pressed=False
s_pressed=False
d_pressed=False
space_pressed=False
left_shift_pressed=False
ctrl_pressed=False
move_x=0
move_y=0
move_z=0
first_mouse=True
sensity=0.1
speed=0.1
last_x=None
last_y=None
hotbar_selection_count=0

def registerCallbacks():
	glfw.set_mouse_button_callback(GameClient.attributes["window"], playerUseMouse)
	glfw.set_scroll_callback(GameClient.attributes["window"], scroll_callback)
	
def playerUseMouse(window, button, action, mods):
	if button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.PRESS:
		px,py,pz,bx,by,bz=GameClient.attributes["local_player"].getTrackedPos(Minecraft.level)
		pos=px,py,pz
		if px!=None and py!=None and pz!=None and (Minecraft.level.getBlock(*pos)==Blocks.AIR or Minecraft.level.getBlock(*pos)==Blocks.VOID):
			Minecraft.level.setBlock(*pos, hotbar[hotbar_selection_count])
			Minecraft.level.getBlock(*pos).onPlace(px,py,pz,bx,by,bz)
			with Minecraft.level.lock:
				Minecraft.level.dirty=True
			GameTickThread.client_tick_event.set()
	if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
		px,py,pz,bx,by,bz=GameClient.attributes["local_player"].getTrackedPos(Minecraft.level)
		pos=bx, by, bz
		if Minecraft.level.getBlock(*pos)!=Blocks.AIR and Minecraft.level.getBlock(*pos)!=Blocks.VOID:
			Minecraft.level.setBlock(*pos, Blocks.AIR)
			with Minecraft.level.lock:
				Minecraft.level.dirty=True
			GameTickThread.client_tick_event.set()

def scroll_callback(window, x_offset, y_offset):
	global hotbar_selection_count
	if y_offset>0:
		hotbar_selection_count-=1
	if y_offset<0:
		hotbar_selection_count+=1
	WorldRenderer.hud_renderer.update(hotbar_selection_count)

def handleInput():
    global w_pressed, a_pressed, s_pressed, d_pressed, space_pressed, left_shift_pressed, ctrl_pressed, first_mouse, last_x, last_y
    window = GameClient.attributes["window"]
    player = GameClient.attributes["local_player"]
    mouse_x, mouse_y = glfw.get_cursor_pos(window)
    if first_mouse:
        last_x = mouse_x
        last_y = mouse_y
        first_mouse = False
    delta_x = mouse_x - last_x
    delta_y = last_y - mouse_y
    last_x = mouse_x
    last_y = mouse_y
    player.yaw += -delta_x * sensity
    player.pitch += delta_y * sensity
    player.pitch = max(-89.0, min(89.0, player.pitch))
    w_pressed = glfw.get_key(window, glfw.KEY_W) == glfw.PRESS
    s_pressed = glfw.get_key(window, glfw.KEY_S) == glfw.PRESS
    a_pressed = glfw.get_key(window, glfw.KEY_A) == glfw.PRESS
    d_pressed = glfw.get_key(window, glfw.KEY_D) == glfw.PRESS
    space_pressed = glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS
    left_shift_pressed = glfw.get_key(window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS
    ctrl_pressed = glfw.get_key(window, glfw.KEY_LEFT_CONTROL) == glfw.PRESS
	
def tickPlayerMovement():
	move_x=0
	move_y=0
	move_z=0
	speed=0.1
	yaw=GameClient.attributes["local_player"].yaw
	if ctrl_pressed:
		speed=0.2
	if w_pressed:
		move_x+=sin(yaw)*speed
		move_z+=cos(yaw)*speed
	if s_pressed:
		move_x-=sin(yaw)*speed
		move_z-=cos(yaw)*speed
	if a_pressed:
		move_x+=sin(yaw+90)*speed
		move_z+=cos(yaw+90)*speed
	if d_pressed:
		move_x+=sin(yaw-90)*speed
		move_z+=cos(yaw-90)*speed
	if space_pressed:
		move_y=speed
	if left_shift_pressed:
		move_y=-speed
	GameClient.attributes["local_player"].setDeltaMovement(move_x, move_y, move_z)
	GameClient.attributes["local_player"].move()
