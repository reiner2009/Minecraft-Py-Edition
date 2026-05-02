print("Starting net.minecraft.client.Main")
import net.minecraft.world.item.Item as item
import net.minecraft.util.math.Raycast as Raycast
import net.minecraft.util.math.ThirtPersonPerspective as ThirtPersonPerspective
import net.minecraft.resources.Config as config
import net.minecraft.world.Time as worldTime
import net.minecraft.client.render.world.SkyRenderer as sky
from net.minecraft.chat.Commands import*
from net.minecraft.entity.player.PlayerEntity import PlayerEntity
from net.minecraft.util.gui.Widgets import*
from net.minecraft.sounds.Sounds import*
from net.minecraft.world.level.Level import setEnv
import sys
import math
import random
import traceback
import time
import argparse
import requests

parser = argparse.ArgumentParser(description="Minecraft Launcher Script")
parser.add_argument("--username", type=str, help="username")
parser.add_argument("--skin", type=str, help="skin texture")
parser.add_argument("--online-skin", type=str, help="skin texture from the internet")
args = parser.parse_args()
username = args.username
online_skin = args.online_skin
if username:
	Playername.set(username)
skin = args.skin
try:
	if online_skin:
		response=requests.get("https://minecraft.tools/download-skin/"+online_skin)
		with open("skin.png", "wb") as f:
			f.write(response.content)
		skin="skin.png"
except:
	pass

tips=[
	"Press 'e' to get more blocks",
	"Move with w, a, s, d",
	"Right klick to place a block",
	"Left klick to break a block",
	"Press t to open the chat",
	"Press v to hide the block preview"
]

x = 0
y = 0
z = 0
camera_x = 0
camera_y = 0
camera_z = 0
speed = 0.2
debug_charts = False
running=True
menu=True
hud_=True
message=True
hotbar_slot_selected=1
fps=60
settings=False
pause_menu=False
state_menu=0
state_settings=1
state_game=2
game_state=state_menu
pause_menu=False
mouse_grab=False
try:
	music_volume=float(config.load_config("music_volume"))
except:
	music_volume=489/2
try:
	ui_volume=float(config.load_config("ui_volume"))
except:
	ui_volume=489/2
try:
	block_sound_volume=float(config.load_config("block_sound_volume"))
except:
	block_sound_volume=489/2
button_click_sound.set_volume((1/489)*ui_volume)
chat=False
running_app=True
block_preview=True
chat=False
running_app=True
container=False
chunklist=None
player=PlayerEntity(False)
player.spawn(0,0,0)
player.setName(Playername.playername)
if skin:
	player.setSkin(skin)
EntityList.entities.append(player)
chat_text=""
camera_x, camera_y, camera_z=0,0,0

setEnv("client")

menu_background_texture=load_texture("assets/minecraft/textures/gui/title/background/menu.png")

def save_level():
	world_x, world_y, world_z=player.get_entity_position()
	yaw, pitch = player.get_entity_facing()
	data=[world_x, world_y, world_z, yaw, pitch, worldTime.t, worldTime.sunriseblend, worldTime.sunsetblend, worldTime.light]
	base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
	world = os.path.join(base_path, "world")
	full_path = os.path.join(world, "level.dat")
	try:
		with open(full_path, "wb") as f:
			pickle.dump(data, f)
	except:
		os.mkdir(world)
		with open(full_path, "wb") as f:
			pickle.dump(data, f)

def load_level():
	base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
	world = os.path.join(base_path, "world")
	full_path = os.path.join(world, "level.dat")
	try:
		with open(full_path, "rb") as f:
			d=pickle.load(f)
		player.spawn(d[0], d[1], d[2], d[3], d[4])
		worldTime.set_tick(d[5], d[6], d[7], d[8])
	except Exception:
		pass

def take_screenshot():
    z = time.localtime()
    filename = f"{z.tm_year}-{z.tm_mon}-{z.tm_mday}_{z.tm_hour}-{z.tm_min}-{z.tm_sec}.png"
    global width, height
    data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    image = pygame.image.fromstring(data, (width, height), "RGB")
    image = pygame.transform.flip(image, False, True)
    base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
    screenshots_path = os.path.join(base_path, "screenshots")
    os.makedirs(screenshots_path, exist_ok=True)
    full_path = os.path.join(screenshots_path, filename)
    pygame.image.save(image, full_path)
    if game_state == state_game:
        show_text("Screenshot saved as " + filename, [255, 255, 255, 255])

def rebuild_chunks():
	global chunklist
	glDeleteLists(chunklist, 1)
	chunklist=build_chunk_display_list()

def place_block_by_player():
	global block_sound_volume
	X,Y,Z,*_= Raycast.get_pos(player)
	try:
		if Raycast.get_neighbour_block(X, Y, Z):
			player.swing("right")
			set_block(X, Y, Z, item.selected_item[hotbar_slot_selected - 1])
			play_dig_sound(sound_categorys_dig[item.selected_item[hotbar_slot_selected - 1]], block_sound_volume)
			rebuild_chunks()
	except Exception as e:
		logger.warning("place_block_by_player failed: " + str(e))

def get_block_by_player():
	global hotbar_slot_selected
	*_,X,Y,Z=Raycast.get_pos(player)
	try:
		if get_block(X, Y, Z) != "air":
			if get_block(X,Y,Z) in item.selected_item:
				hotbar_slot_selected=item.selected_item.index(get_block(X,Y,Z))+1
			else:
				item.add_item(item.ITEM_TEXTUE_MAP[get_block(X, Y, Z)],get_block(X, Y, Z) , hotbar_slot_selected-1)
	except Exception as e:
		logger.warning("get_block_by_player failed: " + str(e))


def break_block_by_player():
	global block_sound_volume
	*_,X,Y,Z= Raycast.get_pos(player)
	try:
		if get_block(X, Y, Z)!="air":
			if get_block(X, Y, Z)=="glass_block":
				play_dig_sound(sound_categorys_dig[get_block(X,Y,Z)+"_break"], block_sound_volume)
			else:
				play_dig_sound(sound_categorys_dig[get_block(X, Y, Z)], block_sound_volume)
			set_block(X,Y,Z, "air")
			rebuild_chunks()
	except Exception as e:
		logger.warning("break_block_by_player failed: " + str(e))

def render_hud():
	global pause_menu, message, hotbar_slot_selected, debug_charts,container
	glColor4f(1,1,1,1)
	if hud_==True:
		if not player.thirt_person_perspective:
			hud.render_crosshair()
		hud.render_hotbar()
		hud.render_hotbar_selection(hotbar_slot_selected)
		if chat==False:
			render_temporary_texts()
		item.render_items_for_hotbar()
	if debug_charts and hud_==True:
		world_x, world_y, world_z=player.get_entity_position()
		yaw, pitch = player.get_entity_facing()
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		hud.display_fps()
		hud.display_position(round(world_x), round(world_y), round(world_z))
		hud.display_rotate(round(yaw),round(pitch))
	if container==True:
		pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
		hud.render_tab_items()
		item.render_items_for_container()

def draw_scene():
	if pause_menu==False:
		worldTime.tick()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	setup_perspective()
	apply_camera()
	sky.render(camera_x/2, camera_y/2, camera_z/2,worldTime.get_light(), worldTime.sunriseblend, worldTime.sunsetblend, worldTime.t)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
	glColor3f(worldTime.get_light(), worldTime.get_light(), worldTime.get_light())
	glCallList(chunklist)
	for p in EntityList.entities:
		p.tick()
	x,y,z,x1,y1,z1= Raycast.get_pos(player)
	if block_preview==True:
		if get_block(x1, y1, z1)!="air":
			draw_block_preview(x1, y1, z1,True)
		if Raycast.get_neighbour_block(x, y, z):
			draw_block_preview(x, y, z)
	setup_ortho()
	render_hud()
	player.setMainhandItem(item.selected_item[hotbar_slot_selected - 1])
    
def apply_camera():
	global camera_x, camera_y, camera_z
	yaw, pitch = player.get_entity_facing()
	if player.thirt_person_perspective==1:
		camera_x, camera_y, camera_z = ThirtPersonPerspective.get_look_direction_behind(5, player)
	elif player.thirt_person_perspective==2:
		pitch=pitch-180
		camera_x, camera_y, camera_z = ThirtPersonPerspective.get_look_direction_front(5, player)
	elif player.thirt_person_perspective==0:
		camera_x, camera_y, camera_z=player.get_entity_position()
	camera_x=camera_x*2
	camera_y=camera_y*2
	camera_z=camera_z*2
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	if player.thirt_person_perspective==2:
		glRotatef(-180, 0, 0, 1)
	glRotatef(pitch, 1, 0, 0)
	glRotatef(yaw, 0, 1, 0)
	glTranslatef(-camera_x, -camera_y, -camera_z)

def render_settings(events):
	global game_state, music_volume, ui_volume, block_sound_volume
	setup_ortho()
	pygame.mixer.music.set_volume((1/489)*music_volume)
	button_click_sound.set_volume((1/489)*ui_volume)
	hud.render_wallpaper(dark_menu_texture)
	x,y=pygame.mouse.get_pos()
	y=height-y
	if round((100/489)*music_volume)>0:
		display_music_volume="Music volume: "+str(round((100/489)*music_volume))+"%"
	else:
		display_music_volume="Music volume: off"
	if round((100/489)*ui_volume)>0:
		display_ui_volume="UI volume: "+str(round((100/489)*ui_volume))+"%"
	else:
		display_ui_volume="UI volume: off"
	if round((100/489)*block_sound_volume)>0:
		display_block_sound_volume="Block Sound Volume: "+str(round((100/489)*block_sound_volume))+"%"
	else:
		display_block_sound_volume="Block Sound Volume: off"
	for event in events:
		if event.type == QUIT:
			pygame.quit()
	x1, x2 = width/2-510/2, width/2+510/2
	y1, y2 = height/480*250, height/480*250+60
	y3, y4 = y1+65, y2+65
	y7, y8 = y3+5, y4+5
	y9, y10 = y7+60, y8+60
	y5, y6 = y9 + 60, y10 + 60
	if x>=x1 and x<=x2 and y>=y1 and y<=y2:
		button(x1, y1, x2, y2, "Done", True)
		slider(x1, y5, x2, y6, False, music_volume, display_music_volume)
		slider(x1, y7, x2, y8, False, ui_volume, display_ui_volume)
		slider(x1, y9, x2, y10, False, block_sound_volume, display_block_sound_volume)
		pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
		for event in events:
			if event.type==MOUSEBUTTONDOWN and event.button==1:
				config.save_config("music_volume", music_volume)
				config.save_config("ui_volume", ui_volume)
				config.save_config("block_sound_volume", block_sound_volume)
				button_click_sound.play()
				game_state=state_menu
	elif x>=x1 and x<=x2 and y>=y5 and y<=y6:
		button(x1, y1, x2, y2, "Done", False)
		slider(x1, y5, x2, y6, True, music_volume, display_music_volume)
		slider(x1, y7, x2, y8, False, ui_volume, display_ui_volume)
		slider(x1, y9, x2, y10, False, block_sound_volume, display_block_sound_volume)
		pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
		mouse_buttons=pygame.mouse.get_pressed()
		if mouse_buttons[0]:
			music_volume=x-x1
			music_volume=max(0, min(489, music_volume))
	elif x>=x1 and x<=x2 and y>=y7 and y<=y8:
		button(x1, y1, x2, y2, "Done", False)
		slider(x1, y5, x2, y6, False, music_volume, display_music_volume)
		slider(x1, y7, x2, y8, True, ui_volume, display_ui_volume)
		slider(x1, y9, x2, y10, False, block_sound_volume, display_block_sound_volume)
		pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
		mouse_buttons=pygame.mouse.get_pressed()
		if mouse_buttons[0]:
			ui_volume=x-x1
			ui_volume=max(0, min(489, ui_volume))
	elif x>=x1 and x<=x2 and y>=y9 and y<=y10:
		button(x1, y1, x2, y2, "Done", False)
		slider(x1, y5, x2, y6, False, music_volume, display_music_volume)
		slider(x1, y7, x2, y8, False, ui_volume, display_ui_volume)
		slider(x1, y9, x2, y10, True, block_sound_volume, display_block_sound_volume)
		pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
		mouse_buttons=pygame.mouse.get_pressed()
		if mouse_buttons[0]:
			block_sound_volume=x-x1
			block_sound_volume=max(0, min(489, block_sound_volume))
	else:
		pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
		button(x1, y1, x2, y2, "Done", False)
		slider(x1, y5, x2, y6, False, music_volume, display_music_volume)
		slider(x1, y7, x2, y8, False, ui_volume, display_ui_volume)
		slider(x1, y9, x2, y10, False, block_sound_volume, display_block_sound_volume)

def render_menu(events):
	global settings, game_state, mouse_grab
	setup_ortho()
	pygame.mixer.music.set_volume((1/489)*music_volume)
	hud.render_wallpaper(menu_background_texture)
	hud.render_title_font()
	hud.render_copyright_text()
	x,y=pygame.mouse.get_pos()
	y=height-y
	if game_state==state_menu:
		play_music_mode(music_menu)
	for event in events:
		if event.type == QUIT:
			pygame.quit()
	x1, x2 = width/2-510/2, width/2+510/2
	y1, y2 = height/480*250, height/480*250+60
	y3, y4 = y1-65, y2-65
	y5, y6 = y3-65, y4-65
	if x>=x1 and x<=x2 and y>=y1 and y<=y2:
		button(x1, y1, x2, y2, "Start game", True)
		button(x1, y3, x2, y4, "Quit game", False)
		button(x1, y5, x2, y6, "Settings", False)
		pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
		for event in events:
			if event.type==MOUSEBUTTONDOWN and event.button==1:
				stop_music()
				button_click_sound.play()
				game_state=state_game
				mouse_grab=True
	elif x>=x1 and x<=x2 and y>=y3 and y<=y4:
		button(x1, y1, x2, y2, "Start game", False)
		button(x1, y3, x2, y4, "Quit game", True)
		button(x1, y5, x2, y6, "Settings", False)
		pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
		for event in events:
			if event.type==MOUSEBUTTONDOWN and event.button==1:
				button_click_sound.play()
				pygame.time.delay(150)
				pygame.quit()
				logger.set_environment("Main")
				logger.info("Stopped!")
				sys.exit()
	elif x>=x1 and x<=x2 and y>=y5 and y<=y6:
		button(x1, y1, x2, y2, "Start game", False)
		button(x1, y3, x2, y4, "Quit game", False)
		button(x1, y5, x2, y6, "Settings", True)
		pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
		for event in events:
			if event.type==MOUSEBUTTONDOWN and event.button==1:
				button_click_sound.play()
				game_state=state_settings
	else:
		button(x1, y1, x2, y2, "Start game", False)
		button(x1, y3, x2, y4, "Quit game", False)
		button(x1, y5, x2, y6, "Settings", False)
		pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)

def running_world(events):
	global menu, running, x,y,z, camera_x, camera_y, camera_z, speed, mouse_grab,hud_,hotbar_slot_selected, debug_charts, game_state, chunklist, pause_menu, mouse_grab, chat, chat_text, block_preview, container
	pygame.mixer.music.set_volume((1/489)*music_volume)
	if chunklist==None:
		render_chunk()
		load_level()
		chunklist = build_chunk_display_list()
		show_text(Playername.playername + " joined the game", [84, 251, 84, 255])
		show_text("[TIP] "+random.choice(tips), [84,84,251,255])
		logger.set_environment("Main")
		logger.info(Playername.playername + " joined the game")
	play_music_mode(music_creative)
	if pause_menu==True:
		pause_music()
	elif pause_menu==False:
		unpause_music()
	for event in events:
		if event.type == QUIT:
			running = False
		elif event.type==KEYDOWN and event.key==K_F1 and pause_menu==False and chat==False and container==False:
			hud_=not hud_
		elif event.type==KEYDOWN and event.key==K_F3 and pause_menu==False and chat==False and container==False:
			debug_charts=not debug_charts
		elif event.type==KEYDOWN and event.key==K_t and chat==False and pause_menu==False and container==False:
			chat=True
			pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
			chat_text=""
		elif event.type==KEYDOWN and event.key==K_e and chat==False and pause_menu==False:
			container=not container
			mouse_grab=not mouse_grab
		elif event.type==KEYDOWN and event.key==K_ESCAPE and container==True:
			container=False
			mouse_grab=True
		elif event.type==KEYDOWN and event.key==K_ESCAPE and chat==False:
			pause_menu=not pause_menu
			mouse_grab=not mouse_grab
		elif event.type==KEYDOWN and event.key==K_v and chat==False and pause_menu==False and container==False:
			block_preview=not block_preview
		if event.type==MOUSEBUTTONDOWN and event.button==3:
			if pause_menu==False and chat==False and container==False:
				place_block_by_player()
		if event.type==MOUSEBUTTONDOWN and event.button==2:
			if pause_menu==False and chat==False and container==False:
				get_block_by_player()
		if event.type==MOUSEBUTTONDOWN and event.button==1:
			if pause_menu==False and chat==False and container==False:
				player.swing("right")
				break_block_by_player()
	if mouse_grab==True:
		pygame.mouse.set_visible(False)
		pygame.event.set_grab(True)
		mx, my = pygame.mouse.get_rel()
		player.rotate(mx*0.1, my*-0.1)
	elif mouse_grab==False:
		pygame.mouse.set_visible(True)
		pygame.event.set_grab(False)
	move_x = 0
	move_z = 0
	move_y = 0
	dx = math.sin(math.radians(player.get_entity_facing()[0]))
	dz = math.cos(math.radians(player.get_entity_facing()[0]))
	dx_side = math.sin(math.radians(player.get_entity_facing()[0] - 90))
	dz_side = math.cos(math.radians(player.get_entity_facing()[0] - 90))
	keys = pygame.key.get_pressed()
	if chat==False and container==False:
		if keys[K_w]:
			move_x -= dx * speed
			move_z -= dz * speed
		if keys[K_s]:
			move_x += dx * speed
			move_z += dz * speed
		if keys[K_a]:
			move_x -= dx_side * speed
			move_z -= dz_side * speed
		if keys[K_d]:
			move_x += dx_side * speed
			move_z += dz_side * speed
		if keys[K_LSHIFT]:
			move_y-=0.1
		if keys[K_SPACE]:
			move_y+=0.1
		if keys[K_LCTRL]:
			speed=0.2				
		else:
			speed=0.1
	player.move(-move_x, move_y,move_z)
	draw_scene()
	if pause_menu==True:
		hud.render_title_font()
		x,y=pygame.mouse.get_pos()
		y=height-y
		x1, x2 = width/2-510/2, width/2+510/2
		y1, y2 = height/480*250, height/480*250+60
		y3, y4 = y1-65, y2-65
		if x>=x1 and x<=x2 and y>=y1 and y<=y2:
			button(x1, y1, x2, y2, "Quit to title", True)
			button(x1, y3, x2, y4, "Back to game", False)
			pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
			for event in events:
				if event.type==MOUSEBUTTONDOWN and event.button==1 and pause_menu==True:
					texts.clear()
					temporary_texts.clear()
					button_click_sound.play()
					pygame.time.delay(150)
					stop_music()
					logger.set_environment("Main")
					logger.info(Playername.playername + " left the game")
					game_state=state_menu
					pygame.mouse.set_visible(True)
					pygame.event.set_grab(False)
					mouse_grab=False
					chunklist=None
					game_state=state_menu
					pause_menu=False
					logger.info("Saving world")
					save_world()
					save_level()
		elif x>=x1 and x<=x2 and y>=y3 and y<=y4:
			button(x1, y3, x2, y4, "Back to game", True)
			button(x1, y1, x2, y2, "Quit to title", False)
			pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
			for event in events:
				if event.type==MOUSEBUTTONDOWN and event.button==1 and pause_menu==True:
					button_click_sound.play()
					pause_menu=False
					unpause_music()
					mouse_grab=not mouse_grab
		else:
			button(x1, y3, x2, y4, "Back to game", False)
			button(x1, y1, x2, y2, "Quit to title", False)
			pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
	for event in events:
		if event.type==KEYDOWN and event.key>=49 and event.key<=57:
			hotbar_slot_selected=event.key-48
		if event.type==MOUSEBUTTONDOWN and container==False and chat==False and pause_menu==False:
			if event.button==5:
				hotbar_slot_selected+=1
				if hotbar_slot_selected>9:
					hotbar_slot_selected=1
			elif event.button==4:
				hotbar_slot_selected-=1
				if hotbar_slot_selected<1:
					hotbar_slot_selected=9
		if event.type==KEYDOWN and event.key==K_F5:
			player.set_thirt_person_perspective()
	if chat==True:
		events=pygame.event.get()
		render_texts()
		mouse_grab=False
		hud.render_chat_background(60, 30)
		text.render_text(chat_text, 15, 60, 20, 20, [255, 255, 255, 255], True)
		for event in events:
			if event.type==KEYDOWN:
				if event.key==K_RETURN:
					mouse_grab=True
					if chat_text != "":
						if chat_text.startswith("/"):
							assume_command(chat_text, player, chunklist)
						else:
							show_text("<" + str(Playername.playername) + "> " + chat_text, [255, 255, 255, 255])
							logger.set_environment("Main")
							logger.info("[CHAT] <" + str(Playername.playername) + "> " + chat_text)
					chat_text=""
					chat=False
				elif event.key==K_ESCAPE:
					mouse_grab=True
					chat_text=""
					chat=False
				elif event.key==K_BACKSPACE:
					chat_text=chat_text[:-1]
				elif event.key==K_F2:
					take_screenshot()
				else:
					chat_text=chat_text+event.unicode

try:
	while running_app:
		if chat==False:
			events=pygame.event.get()
		for event in events:
			if event.type==QUIT and game_state==state_game:
				save_world()
				save_level()
				running_app=False
			elif event.type==KEYDOWN and event.key==K_F2:
				take_screenshot()
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		pygame.display.set_caption("Minecraft")
		item.set_vars(events, hotbar_slot_selected)
		if game_state==state_menu:
			render_menu(events)
		elif game_state==state_settings:
			render_settings(events)
		elif game_state==state_game:
			running_world(events)
		pygame.display.flip()
		clock.tick(60)
except Exception:
	crash=traceback.format_exc()
	logger.set_environment("Main")
	logger.error(crash)
	save_level()
	save_world()
