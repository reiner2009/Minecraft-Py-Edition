from opensimplex import OpenSimplex
import json
import random
import hashlib
import net.mcpy.resources.FileLoader as FileLoader
import net.mcpy.client.GameClient as GameClient
import net.mcpy.registry.Registry as Registry
import net.mcpy.registry.Registries as Registries
from net.mcpy.resources.ResourceLocation import ResourceLocation
from net.mcpy.world.generator.Tree import Tree
from net.mcpy.world.level.Level import Level

noise_settings=json.load(open(FileLoader.getFromModOrFrozen("data/minecraft/worldgen/noise_settings/overworld.json")))

def createRng(world_seed, name, x, y, z):
	data=f"{world_seed}:{name}:{x}:{y}:{z}"
	seed=int.from_bytes(hashlib.sha256(data.encode()).digest(), "big")
	return random.Random(seed)

def getNoise(x,z, noise):
	ay=0
	for noise_freq in noise_settings["terrian"]:
		ay+=round(noise.noise2(x * noise_freq["freq_x"], z * noise_freq["freq_z"])*noise_freq["amplitude"])
	return ay+noise_settings["height"]

def isSpaghettiCave(x,y,z, cave_noise_0, cave_noise_1):
	spaghetti_caves=noise_settings["spaghetti_caves"]
	freq_x=spaghetti_caves["freq_x"]
	freq_y=spaghetti_caves["freq_y"]
	freq_z=spaghetti_caves["freq_z"]
	amplitude=spaghetti_caves["amplitude"]
	trestle_value=spaghetti_caves["trestle_value"]
	n0=cave_noise_0.noise3(x*freq_x, y*freq_y, z*freq_z) * amplitude
	n1=cave_noise_1.noise3(x*freq_x, y*freq_y, z*freq_z) * amplitude
	return max(abs(n0), abs(n1)) < trestle_value

def generateWorld(seed):
	world_size=noise_settings["world_size"]
	level=Level()
	noise=OpenSimplex(seed=seed)
	cave_noise_0=OpenSimplex(seed=seed+1)
	cave_noise_1=OpenSimplex(seed=seed+2)
	features={}
	for feature_data in Registry.registries[Registries.FEATURE]:
		resource_location=feature_data[0]
		feature=feature_data[1]
		features[resource_location]=[
			feature,
			json.load(open(FileLoader.getFromModOrFrozen("data/"+resource_location.namespace+"/worldgen/features/"+resource_location.path+".json")))
		]
	for x in range(world_size*8):
		for z in range(world_size*8):
			ay=getNoise(x,z, noise)
			level.setBlock(x,-11,z, ResourceLocation(path="bedrock"))
			for y in range(-10, ay+1):
				if y < 0:
					level.setBlock(x,y,z, ResourceLocation(path="deepslatey"))
				else:
					level.setBlock(x,y,z, ResourceLocation(path="stone"))
			level.setBlock(x,ay+1,z, ResourceLocation(path="dirt"))
			level.setBlock(x,ay+2,z, ResourceLocation(path="grass_block"))
			for y in range(-8, ay+3):
				if isSpaghettiCave(x,y,z, cave_noise_0, cave_noise_1):
					level.setBlock(x,y,z,ResourceLocation(path="air"))
			for resource_location, feature_content in features.items():
				feature_class=feature_content[0]
				feature_data=feature_content[1]
				rng=createRng(seed, resource_location, x, ay+3, z)
				feature=feature_class(rng)
				min_chance=feature_data["spawn_chance"]["min"]
				max_chance=feature_data["spawn_chance"]["max"]
				can_spawn_at=feature_data["spawn_chance"]["can_spawn_at"]
				if rng.randint(min_chance, max_chance)==can_spawn_at and feature.checkSpawnRules(level, x, ay+2, z):
					feature.place(level, x, ay+3, z)
	return level
