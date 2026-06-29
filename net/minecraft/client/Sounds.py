from net.minecraft.client import*
import random
import net.minecraft.resources.DataLocation as DataLocation
import net.minecraft.util.Logger as logger
import json

next_music_time=0
music_paused=False
music_menu=0
music_creative=1
current_music_mode=None
sound_data=json.load(open(DataLocation.get_resource_path("assets/minecraft/sounds/sounds.json")))

button_click_sound=pygame.mixer.Sound(DataLocation.get_resource_path("assets/minecraft/sounds/gui/"+sound_data["gui"]["button"]+".ogg"))
button_channel=pygame.mixer.Channel(0)

creative_music_tracks_path= "assets/minecraft/sounds/music/game/creative/"
menu_music_tracks_path= "assets/minecraft/sounds/music/menu/"
dig_music_tracks_path= "assets/minecraft/sounds/random/dig/"

creative_music_tracks=[]

for i in sound_data["music"]["creative"]:
	creative_music_tracks.append(creative_music_tracks_path+i+".ogg")

menu_music_tracks=[]

for i in sound_data["music"]["menu"]:
	menu_music_tracks.append(menu_music_tracks_path+i+".ogg")

glass_music_tracks=[
	"assets/minecraft/sounds/random/glass1.ogg",
	"assets/minecraft/sounds/random/glass2.ogg",
	"assets/minecraft/sounds/random/glass3.ogg"
]

def play_music_mode(mode):
	global current_music_mode, next_music_time, music_paused
	now=pygame.time.get_ticks()
	if current_music_mode != mode:
		pygame.mixer.music.stop()
		current_music_mode=mode
		next_music_time=0
		music_paused=False
	if music_paused:
		return	
	if pygame.mixer.music.get_busy():
		return
	if now < next_music_time:
		return
	if mode==music_menu:
		track=random.choice(menu_music_tracks)
	elif mode==music_creative:
		track=random.choice(creative_music_tracks)
	else:
		return
	pygame.mixer.music.load(DataLocation.get_resource_path(track))
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play()
	delay=random.randint(20000, 60000)
	next_music_time=now+delay
	

def pause_music():
	global music_paused
	if pygame.mixer.music.get_busy():
		pygame.mixer.music.pause()
		music_paused=True
		
def unpause_music():
	global music_paused
	if music_paused:
		pygame.mixer.music.unpause()
		music_paused=False
		
def stop_music():
	pygame.mixer.stop()
	global music_paused
	music_paused=False

def play_place_sound(name, v):
	try:
		block_sound = random.choice(sound_data["blocks"]["place"][name])
		sound = pygame.mixer.Sound(DataLocation.get_resource_path("assets/minecraft/sounds/blocks/place/"+block_sound+".ogg"))
	except Exception as e:
		logger.warning(str(e))
		sound = pygame.mixer.Sound(DataLocation.get_resource_path("assets/minecraft/sounds/blocks/place/stone"+str(random.randint(1,4))+".ogg"))
	sound.set_volume((1/489)*v)
	sound.play()

def play_break_sound(name, v):
	try:
		block_sound = random.choice(sound_data["blocks"]["break"][name])
		sound = pygame.mixer.Sound(DataLocation.get_resource_path("assets/minecraft/sounds/blocks/break/" + block_sound + ".ogg"))
	except Exception as e:
		logger.warning(str(e))
		sound = pygame.mixer.Sound(DataLocation.get_resource_path("assets/minecraft/sounds/blocks/place/stone"+str(random.randint(1,4))+".ogg"))
	sound.set_volume((1 / 489) * v)
	sound.play()

def play_block_sound(name, v):
	try:
		block_sound = random.choice(sound_data["blocks"]["generic"][name])
		sound = pygame.mixer.Sound(DataLocation.get_resource_path("assets/minecraft/sounds/blocks/generic/" + block_sound + ".ogg"))
	except Exception as e:
		logger.warning(str(e))
		sound = pygame.mixer.Sound(DataLocation.get_resource_path("assets/minecraft/sounds/blocks/place/stone"+str(random.randint(1,4))+".ogg"))
	sound.set_volume((1 / 489) * v)
	sound.play()
