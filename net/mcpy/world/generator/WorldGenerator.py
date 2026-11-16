from opensimplex import OpenSimplex
import json
import random
import net.mcpy.resources.FileLoader as FileLoader
import net.mcpy.client.GameClient as GameClient
from net.mcpy.resources.ResourceLocation import ResourceLocation
from net.mcpy.world.generator.Tree import Tree
from net.mcpy.world.level.Level import Level

def generateWorld(seed):
	level=Level()
	noise_settings=json.load(open(FileLoader.getFromModOrFrozen("data/minecraft/worldgen/noise_settings/overworld.json")))
	noise=OpenSimplex(seed=seed)
	for x in range(noise_settings["world_scale"]):
		for z in range(noise_settings["world_scale"]):
			value=noise.noise2(x * noise_settings["x"], z * noise_settings["z"])*noise_settings["hilly_intensity"]+noise_settings["terrian_height"]
			ay=round(value)
			level.setBlock(x,-11,z, ResourceLocation(path="bedrock"))
			for y in range(-10, 0):
				level.setBlock(x,y,z, ResourceLocation(path="deepslatey"))
			for y in range(ay+1):
				level.setBlock(x,y,z, ResourceLocation(path="stone"))
			level.setBlock(x,ay+1,z, ResourceLocation(path="dirt"))
			level.setBlock(x,ay+2,z, ResourceLocation(path="grass_block"))
			tree=Tree()
			if random.randint(0, 50)==1 and tree.checkSpawnRules(level, x, ay+2, z):
				tree.place(level, x, ay+3, z)
	spawn_pos=round(noise_settings["world_scale"]/2)
	try:
		GameClient.attributes["local_player"].spawn(spawn_pos,round(noise.noise2(spawn_pos * noise_settings["x"], spawn_pos * noise_settings["z"])*noise_settings["hilly_intensity"]+noise_settings["terrian_height"]+1), spawn_pos)
	except KeyError:
		pass
	return level
