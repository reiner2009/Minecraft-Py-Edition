import json
import net.minecraft.resources.DataLocation as DataLocation

def get_feature_list(feature):
    data=json.load(open(DataLocation.get_resource_path("data/minecraft/worldgen/feature/"+feature+"/config.json")))
    return data