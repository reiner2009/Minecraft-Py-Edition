import platform

def get_save_system():
	system=platform.system()
	if system=="Windows":
		return "APPDATA"
	else:
		return "HOME"
