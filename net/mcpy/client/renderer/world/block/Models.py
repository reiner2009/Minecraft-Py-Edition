import json
import net.mcpy.resources.FileLoader as FileLoader
import net.mcpy.registry.Registry as Registry
from net.mcpy.resources.Identifier import Identifier

atlas_data=json.load(open("assets/minecraft/atlas_data/blocks.json"))
width=atlas_data["width"]
height=atlas_data["height"]
uv=atlas_data["uv"]

def load_model(id):
	name=id.path
	try:
		model=json.load(open(FileLoader.getFromModOrFrozen("assets/"+id.namespace+"/models/block/"+name+".json")))
		return model
	except FileNotFoundError:
		if name in uv.keys():
			return {"type":"full_cube", "textures":[name, name, name, name, name, name]}
		else:
			return {"type":"full_cube", "textures":["missing","missing","missing","missing","missing","missing"]}

models={}
def init():
	for registry in Registry.registries["block"]:
		id=registry[0]
		all_block_states=registry[1].getBlockState()["all"]
		for state in all_block_states:
			models[id.getAsString()+state]=load_model(Identifier(path=id.path+state))