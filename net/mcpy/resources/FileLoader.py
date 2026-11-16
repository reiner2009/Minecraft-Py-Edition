import os
import platform
import sys
import zipfile

def getSystemId():
	system=platform.system()
	if system=="Windows":
		return "APPDATA"
	else:
		return "HOME"

def getFrozenFile(path):
	if getattr(sys, 'frozen', False):
		base_path=sys._MEIPASS
	else:
		base_path=os.path.abspath(".")
	return os.path.join(base_path, path)

def loadFileFromMod(path):
	base_path = os.path.join(os.environ[getSystemId()], ".minecraft-py")
	mod_path=os.path.join(base_path, ".cache/mods")
	if os.path.exists(os.path.join(mod_path, path)):
		return(os.path.join(mod_path, path))
	else:
		return getFrozenFile(path)

def getFromModOrFrozen(path):
	pack=""
	try:
		base_path = os.path.join(os.environ[getSystemId()], ".minecraft-py")
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
			return loadFileFromMod(path)
	except:
		return loadFileFromMod(path)
		
