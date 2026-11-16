import json
from net.mcpy.resources.ResourceLocation import ResourceLocation
import net.mcpy.resources.FileLoader as FileLoader
import net.mcpy.registry.Registry as Registry

atlas_data=json.load(open("assets/minecraft/atlas_data/blocks.json"))
width=atlas_data["width"]
height=atlas_data["height"]
uv=atlas_data["uv"]

def load_model(resource_location):
	name=resource_location.path
	try:
		model=json.load(open(FileLoader.getFromModOrFrozen("assets/"+resource_location.namespace+"/models/block/"+name+".json")))
		return model
	except FileNotFoundError:
		if name in uv.keys():
			return {"type":"full_cube", "textures":[name, name, name, name, name, name]}
		else:
			return {"type":"full_cube", "textures":["missing","missing","missing","missing","missing","missing"]}

models={}
def init():
	for registry in Registry.registries["block"]:
		resource_location=registry[0]
		models[resource_location.getAsString()]=load_model(resource_location)
