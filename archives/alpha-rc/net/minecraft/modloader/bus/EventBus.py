import net.minecraft.modloader.core.registry.BuiltInRegistries as BuiltInRegistries
import net.minecraft.modloader.ModLoader as ModLoader
import net.minecraft.util.Logger as Logger
from net.minecraft.client.game.GameStates import *

class EventBus:
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

class RegistryEventBus(EventBus):
	def __init__(self, LOGGER_ENV):
		super().__init__(LOGGER_ENV)
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

class TickEventBus(EventBus):
	def __init__(self, LOGGER_ENV):
		super().__init__(LOGGER_ENV)
	def setGameState(self, state):
		global game_state
		game_state=state
	def getGameState(self):
		return game_state

class StartupEventBus(EventBus):
	def __init__(self, LOGGER_ENV):
		super().__init__(LOGGER_ENV)

class ShutdownEventBus(EventBus):
	def __init__(self, LOGGER_ENV):
		super().__init__(LOGGER_ENV)

registryEventBus=RegistryEventBus("ModLoader")
tickEventBus=TickEventBus("ModLoader")
startupEventBus=StartupEventBus("ModLoader")
shutdownEventBus=ShutdownEventBus("ModLoader")

ModLoader.dispatch(RegistryEventBus, registryEventBus)
ModLoader.dispatch(StartupEventBus, startupEventBus)
