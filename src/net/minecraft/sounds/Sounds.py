from net.minecraft.client.Client import*
import random

next_music_time=0
music_paused=False
music_menu=0
music_creative=1
current_music_mode=None

button_click_sound=pygame.mixer.Sound("assets/minecraft/sounds/random/click.ogg")
button_channel=pygame.mixer.Channel(0)

creative_music_tracks_path= "assets/minecraft/sounds/music/game/creative/"
menu_music_tracks_path= "assets/minecraft/sounds/music/menu/"
dig_music_tracks_path= "assets/minecraft/sounds/random/dig/"

creative_music_tracks=[
	creative_music_tracks_path+"creative1.ogg",
	creative_music_tracks_path+"creative2.ogg",
	creative_music_tracks_path+"creative3.ogg",
	creative_music_tracks_path+"creative4.ogg",
	creative_music_tracks_path+"creative5.ogg",
	creative_music_tracks_path+"creative6.ogg",
	creative_music_tracks_path+"creative7.ogg",
	creative_music_tracks_path+"creative8.ogg",
	creative_music_tracks_path+"creative9.ogg",
	creative_music_tracks_path+"creative10.ogg",
	creative_music_tracks_path+"creative11.ogg",
	creative_music_tracks_path+"creative12.ogg",
	creative_music_tracks_path+"creative13.ogg",
	creative_music_tracks_path+"creative14.ogg",
	creative_music_tracks_path+"creative15.ogg",
	creative_music_tracks_path+"creative16.ogg",
	creative_music_tracks_path+"creative17.ogg",
	creative_music_tracks_path+"creative18.ogg",
	creative_music_tracks_path+"creative19.ogg",
]

menu_music_tracks=[
	menu_music_tracks_path+"menu1.ogg",
	menu_music_tracks_path+"menu2.ogg",
	menu_music_tracks_path+"menu3.ogg",
	menu_music_tracks_path+"menu4.ogg",
	menu_music_tracks_path+"menu5.ogg",
	menu_music_tracks_path+"menu6.ogg",
	menu_music_tracks_path+"menu7.ogg",
	menu_music_tracks_path+"menu8.ogg",
	menu_music_tracks_path+"menu9.ogg",
	menu_music_tracks_path+"menu10.ogg",
	menu_music_tracks_path+"menu11.ogg",
	menu_music_tracks_path+"menu12.ogg",
	menu_music_tracks_path+"menu13.ogg",
	menu_music_tracks_path+"menu14.ogg",
	menu_music_tracks_path+"menu15.ogg",
]

dig_stone_music_tracks=[
	dig_music_tracks_path+"stone1.ogg",
	dig_music_tracks_path+"stone2.ogg",
	dig_music_tracks_path+"stone3.ogg",
	dig_music_tracks_path+"stone4.ogg",
]

dig_grass_music_tracks=[
	dig_music_tracks_path+"grass1.ogg",
	dig_music_tracks_path+"grass2.ogg",
	dig_music_tracks_path+"grass3.ogg",
	dig_music_tracks_path+"grass4.ogg",
]

dig_wood_music_tracks=[
	dig_music_tracks_path+"wood1.ogg",
	dig_music_tracks_path+"wood2.ogg",
	dig_music_tracks_path+"wood3.ogg",
	dig_music_tracks_path+"wood4.ogg",
]

dig_gravel_music_tracks=[
	dig_music_tracks_path+"gravel1.ogg",
	dig_music_tracks_path+"gravel2.ogg",
	dig_music_tracks_path+"gravel3.ogg",
	dig_music_tracks_path+"gravel4.ogg",
]

dig_cloth_music_tracks=[
	dig_music_tracks_path+"cloth1.ogg",
	dig_music_tracks_path+"cloth2.ogg",
	dig_music_tracks_path+"cloth3.ogg",
	dig_music_tracks_path+"cloth4.ogg",
]

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
	pygame.mixer.music.load(track)
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play()
	delay=random.randint(2000, 6000)
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

def play_dig_sound(category, v):
	block_sound = random.choice(category)
	sound = pygame.mixer.Sound(block_sound)
	sound.set_volume((1/489)*v)
	sound.play()
