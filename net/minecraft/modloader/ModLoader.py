import net.minecraft.resources.DataLocation as DataLocation
import net.minecraft.util.Logger as logger
from net.minecraft.util.Debug import debugMode
import sys
import os
import traceback
import zipfile
import inspect 

base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
modfolder = os.path.join(base_path, "mods")
os.makedirs(modfolder, exist_ok=True)
modfile=os.path.join(modfolder, "mod.zip")
MOD=False

try:
	temp_dir=os.path.join(base_path, ".cache/mods")
	with zipfile.ZipFile(modfile, "r") as zipf:
		zipf.extractall(temp_dir)
	if os.path.exists(temp_dir):
		sys.path.append(temp_dir)
except:
	pass

def dispatch(eventBusType, eventBus):
	try:
		try:
			import mod
		except:
			if debugMode==True:
				logger.error(str(traceback.format_exc()))
		try:
			for name, obj in inspect.getmembers(mod):
				if hasattr(obj, "is_event_handler"):
					if obj.event_type == eventBusType:
						obj(eventBus)
		except:
			if debugMode==True:
				logger.error(str(traceback.format_exc()))
	except:
		logger.error(str(traceback.format_exc()))

