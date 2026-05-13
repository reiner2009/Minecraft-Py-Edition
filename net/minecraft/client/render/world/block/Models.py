import json
import net.minecraft.util.logger.Logger as logger
import net.minecraft.resources.DataLocation as DataLocation
from net.minecraft.world.block.Blocks import registries

models=[]
model_names=[]
for name_, name in registries.items():
	for property in name(name_).getProperties():
		model_names.append(name(name_).getName()+property)

def load_model(name):
	logger.set_environment("Client")
	try:
		with open(DataLocation.get_resource_path(f"assets/minecraft/models/block/{name}.json"), "r") as f:
			models.append(json.load(f))
	except:
		logger.error(f"Failed to load model assets/minecraft/models/block/{name}.json")
		models.append({"textures":["error","error","error","error","error","error"]})
		
	
for i in model_names:
	load_model(i)

model_map={}

for m, i in zip(model_names, range(len(models))):
	model_map[m]=models[i]

def get_model(name, property=""):
	return (model_map[name + property])