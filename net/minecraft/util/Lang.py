import json
import net.minecraft.util.Logger as logger
import net.minecraft.resources.DataLocation as DataLocation

lang={}

try:
    with open(DataLocation.get_resource_path("assets/minecraft/lang/en_us.json"), "r") as f:
        lang=json.load(f)
except Exception as e:
    logger.error(f"Failed to load the language file: " + str(e))

def get_lang_key(key):
    try:
        return lang[key]
    except:
        return key
