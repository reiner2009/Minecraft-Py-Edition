from net.minecraft.modloader.common import SubscribeEvent
from net.minecraft.modloader.bus.EventBus import StartupEventBus, RegistryEventBus, ShutdownEventBus
import net.minecraft.modloader.core.registry.BuiltInRegistries as BuiltInRegistries
from LuckyBlock import LuckyBlock

MODID="luckyblock"

@SubscribeEvent(StartupEventBus)
def onStartup(startupEventBus):
	startupEventBus.info("Starting "+MODID)

@SubscribeEvent(RegistryEventBus)
def registerBlocks(registryEventBus):
	registryEventBus.register(BuiltInRegistries.BLOCK, MODID, "lucky_block", LuckyBlock)
	registryEventBus.info("Registered blocks for "+MODID)

@SubscribeEvent(RegistryEventBus)
def itemGroupEvents(registryEventBus):
	registryEventBus.register(BuiltInRegistries.ITEM_GROUP_ENTRIES, MODID, "lucky_block")
	registryEventBus.info("Registered item group entries for "+MODID)

@SubscribeEvent(ShutdownEventBus)
def onShutdown(shutdownEventBus):
	shutdownEventBus.info("Shutting down "+MODID)