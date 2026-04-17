import json
import net.minecraft.util.logger.Logger as logger

models=[]
model_names=["bedrock", "cobblestone", "deepslate", "dirt", "grass_block", "oak_log", "oak_planks", "stone", "stone_bricks", "white_wool", "light_blue_wool", "green_wool","black_wool","blue_wool","brown_wool","cyan_wool", "gray_wool","light_gray_wool","lime_wool","magenta_wool","orange_wool","pink_wool","purple_wool","red_wool","yellow_wool","oak_leaves","glass_block", "smooth_stone", "gold_block", "diamond_block", "lapis_block", "iron_block"]

def load_model(name):
	try:
		with open(f"assets/minecraft/models/block/{name}.json", "r") as f:
			models.append(json.load(f))
		logger.info(f"Loaded model assets/minecraft/models/block/{name}.json")
	except:
		logger.error(f"Failed to load model assets/minecraft/models/block/{name}.json")
		models.append({"textures":["error","error","error","error","error","error"]})
		
	
for i in model_names:
	load_model(i)

model_map={
	"bedrock":models[0],
	"cobblestone":models[1],
	"deepslate":models[2],
	"dirt":models[3],
	"grass_block":models[4],
	"oak_log":models[5],
	"oak_planks":models[6],
	"stone":models[7],
	"stone_bricks":models[8],
	"white_wool":models[9],
	"light_blue_wool":models[10],
	"green_wool":models[11],
	"black_wool":models[12],
    "blue_wool":models[13],
    "brown_wool":models[14],
    "cyan_wool":models[15],
    "gray_wool":models[16],
    "light_gray_wool":models[17],
    "lime_wool":models[18],
    "magenta_wool":models[19],
    "orange_wool":models[20],
    "pink_wool":models[21],
    "purple_wool":models[22],
    "red_wool":models[23],
    "yellow_wool":models[24],
	"oak_leaves":models[25],
	"glass_block":models[26],
	"smooth_stone":models[27],
	"gold_block":models[28],
	"diamond_block":models[29],
	"lapis_block":models[30],
	"iron_block":models[31]
}

def get_model(name):
	return(model_map[name])
