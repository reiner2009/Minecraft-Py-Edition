import net.minecraft.modloader.core.registry.BuiltInRegistries as BuiltInRegistries
import net.minecraft.modloader.ModLoader as ModLoader

class EventBusRegistry:
	def __init__(self):
		self.REGISTRIES={}
	def register(self, registry, namespace, name, class_):
		self.REGISTRIES[(namespace, name)]=class_
	def get(self):
		return self.REGISTRIES

eventBus=EventBusRegistry()

ModLoader.startup(eventBus)

