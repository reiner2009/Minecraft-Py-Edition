import net.minecraft.resources.DataLocation as DataLocation
import sys
import os
import traceback
import zipfile
import inspect

base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
modfolder = os.path.join(base_path, "mods")
os.makedirs(modfolder, exist_ok=True)
modfile=os.path.join(modfolder, "mod.zip")

try:
	temp_dir=os.path.join(base_path, ".cache/mods")
	with zipfile.ZipFile(modfile, "r") as zipf:
		zipf.extractall(temp_dir)
	if os.path.exists(temp_dir):
		sys.path.append(temp_dir)
except:
	pass

def onStartup():
	try:
		import mod
		from net.minecraft.modloader.bus.EventBus import StartupEventBus, startupEventBus
		try:
			for name, obj in inspect.getmembers(mod):
				if hasattr(obj, "is_event_handler"):
					if obj.event_type == StartupEventBus:
						obj(startupEventBus)
		except AttributeError:
			pass
	except:
		print(traceback.format_exc())

def initRegistry():
	try:
		import mod
		from net.minecraft.modloader.bus.EventBus import EventBusRegistry, eventBusRegistry
		try:
			for name, obj in inspect.getmembers(mod):
				if hasattr(obj, "is_event_handler"):
					if obj.event_type == EventBusRegistry:
						obj(eventBusRegistry)
		except AttributeError:
			pass
	except:
		print(traceback.format_exc())

def onShutdown():
	try:
		import mod
		from net.minecraft.modloader.bus.EventBus import ShutdownEventBus, shutdownEventBus
		try:
			for name, obj in inspect.getmembers(mod):
				if hasattr(obj, "is_event_handler"):
					if obj.event_type == ShutdownEventBus:
						obj(shutdownEventBus)
		except AttributeError:
			pass
	except:
		print(traceback.format_exc())

def tick():
	try:
		import mod
		from net.minecraft.modloader.bus.EventBus import StaticEventBus, staticEventBus
		try:
			for name, obj in inspect.getmembers(mod):
				if hasattr(obj, "is_event_handler"):
					if obj.event_type == StaticEventBus:
						obj(staticEventBus)
		except AttributeError:
			pass
	except:
		print(traceback.format_exc())
