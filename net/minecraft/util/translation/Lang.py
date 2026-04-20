import json
import net.minecraft.util.logger.Logger as logger

lang={}

try:
    with open("assets/minecraft/lang/en_us.json", "r") as f:
        lang=json.load(f)
except Exception as e:
    logger.error(f"Failed to load the language file: " + str(e))

def get_lang_key(key):
    try:
        return lang[key]
    except:
        return key