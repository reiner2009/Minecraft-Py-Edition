from net.minecraft.modloader.common import SubscribeEvent
from net.minecraft.modloader.bus.EventBus import StartupEventBus, EventBusRegistry, StaticEventBus, ShutdownEventBus
import net.minecraft.modloader.core.registry.BuiltInRegistries as BuiltInRegistries
from net.minecraft.world.block import Block

MODID="examplemod"

@SubscribeEvent(StartupEventBus)
def onStartup(startupEventBus):
	startupEventBus.info("Starting "+MODID)

@SubscribeEvent(EventBusRegistry)
def initRegistry(eventBusRegistry):
	eventBusRegistry.register(BuiltInRegistries.BLOCK, MODID, "example_block", Block)

@SubscribeEvent(StaticEventBus)
def tick(staticEventBus):
	staticEventBus.info("tick")

@SubscribeEvent(ShutdownEventBus)
def onShutdown(shutdownEventBus):
	shutdownEventBus.info("Shutting down "+MODID)
