import net.minecraft.modloader.core.registry.BuiltInRegistries as BuiltInRegistries
import net.minecraft.modloader.ModLoader as ModLoader
import net.minecraft.util.Logger as Logger

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
	def getItemGroupEntries(self):
		return BuiltInRegistries.ITEM_GROUP_ENTRIES

class StaticEventBus:
	def __init__(self, LOGGER_ENV):
		self.LOGGER_ENV=LOGGER_ENV
	def getLogger(self):
		return self.LOGGER_ENV
	def info(self, msg):
		Logger.info(msg, self.LOGGER_ENV)
	def warn(self, msg):
		Logger.warn(msg, self.LOGGER_ENV)
	def error(self, msg):
		Logger.error(msg, self.LOGGER_ENV)

class StartupEventBus(StaticEventBus):
	def __init__(self, LOGGER_ENV):
		super().__init__(LOGGER_ENV)

class ShutdownEventBus(StaticEventBus):
	def __init__(self, LOGGER_ENV):
		super().__init__(LOGGER_ENV)

eventBusRegistry=EventBusRegistry()
staticEventBus=StaticEventBus("ModLoader")
startupEventBus=StartupEventBus("ModLoader")
shutdownEventBus=ShutdownEventBus("ModLoader")

ModLoader.initRegistry()
ModLoader.onStartup()
