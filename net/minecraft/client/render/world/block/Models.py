import json
import net.minecraft.util.logger.Logger as logger
import net.minecraft.resources.DataLocation as DataLocation

models=[]
model_names=["bedrock", "cobblestone", "deepslate", "dirt", "grass_block", "oak_log", "oak_planks", "stone", "stone_bricks", "white_wool", "light_blue_wool", "green_wool","black_wool","blue_wool","brown_wool","cyan_wool", "gray_wool","light_gray_wool","lime_wool","magenta_wool","orange_wool","pink_wool","purple_wool","red_wool","yellow_wool","oak_leaves","glass_block", "smooth_stone", "gold_block", "diamond_block", "lapis_block", "iron_block", "bricks","deepslate_bricks","polished_deepslate", "copper_block"]

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

def get_model(name):
	return(model_map[name])
