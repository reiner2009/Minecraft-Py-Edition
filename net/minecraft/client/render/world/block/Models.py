import json
import net.minecraft.util.Logger as logger
import net.minecraft.resources.DataLocation as DataLocation
from net.minecraft.world.block.Blocks import registries, modregistries

models=[]
model_names=[]
itemModels = json.load(open(DataLocation.get_resource_path("assets/minecraft/models/ItemModels.json")))
for name_, name in registries.items():
	for property in name(name_).getProperties():
		model_names.append(name(name_).getName()+property)
for name in itemModels.values():
	model_names.append(name)


def load_model(name, namespace="minecraft"):
	logger.set_environment("Client")
	try:
		with open(DataLocation.get_resource_path(f"assets/{namespace}/models/block/{name}.json"), "r") as f:
			models.append(json.load(f))
	except:
		logger.error(f"Failed to load model assets/{namespace}/models/block/{name}.json")
		models.append({"type":"full_cube","textures":["missing","missing","missing","missing","missing","missing"]})
		
	
for i in model_names:
	if i in modregistries.keys():
		load_model(i, modregistries[i])
	else:
		load_model(i)

model_map={}

for m, i in zip(model_names, range(len(models))):
	model_map[m]=models[i]

def get_model(name, property=""):
	return (model_map[name + property])

def get_item_model(name):
	if name in list(itemModels.keys()):
		return (model_map[itemModels[name]])
	else:
		return (model_map[name])
