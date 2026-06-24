import net.minecraft.resources.DataLocation as DataLocation
import sys
import os
import traceback
import zipfile

base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
modfolder = os.path.join(base_path, "mods")
os.makedirs(modfolder, exist_ok=True)
modfile=os.path.join(modfolder, "mod.zip")

def startup(eventBus):
	try:
		temp_dir=os.path.join(base_path, ".cache/mods")
		with zipfile.ZipFile(modfile, "r") as zipf:
			zipf.extractall(temp_dir)
		if os.path.exists(temp_dir):
			sys.path.append(temp_dir)
			import mod
			mod.onStartup(eventBus)
	except FileNotFoundError:
		pass
