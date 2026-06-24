import os
import platform
import sys
import zipfile

def get_save_system():
	system=platform.system()
	if system=="Windows":
		return "APPDATA"
	else:
		return "HOME"

def get_resource_path_finally(path):
	if getattr(sys, 'frozen', False):
		base_path=sys._MEIPASS
	else:
		base_path=os.path.abspath(".")
	return os.path.join(base_path, path)

def load_from_mod(path):
	base_path = os.path.join(os.environ[get_save_system()], ".minecraft-py")
	mod_path=os.path.join(base_path, ".cache/mods")
	if os.path.exists(os.path.join(mod_path, path)):
		return(os.path.join(mod_path, path))
	else:
		return get_resource_path_finally(path)

def get_resource_path(path):
	pack=""
	try:
		base_path = os.path.join(os.environ[get_save_system()], ".minecraft-py")
		if path.startswith("assets/minecraft"):
			pack = os.path.join(base_path, "resourcepacks/pack.zip")
		if path.startswith("data/minecraft"):
			pack = os.path.join(base_path, "datapacks/pack.zip")
		temp_dir=os.path.join(base_path, ".cache")
		with zipfile.ZipFile(pack, "r") as zipf:
			zipf.extractall(temp_dir)
		if os.path.exists(os.path.join(temp_dir, path)):
			return os.path.join(temp_dir, path)
		else:
			return load_from_mod(path)
	except:
		return load_from_mod(path)
		
