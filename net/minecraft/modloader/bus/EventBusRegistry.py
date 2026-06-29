import net.minecraft.modloader.core.registry.BuiltInRegistries as BuiltInRegistries
import net.minecraft.modloader.ModLoader as ModLoader

class EventBusRegistry:
	def __init__(self):
		pass
	def register(self, registry, namespace, name, class_=None):
		registry[(namespace, name)]=class_
	def getBlocks(self):
		return BuiltInRegistries.BLOCK
	def getItems(self):
		return BuiltInRegistries.ITEM
	def getEntities(self):
		return BuiltInRegistries.ENTITY

eventBus=EventBusRegistry()

ModLoader.startup(eventBus)

