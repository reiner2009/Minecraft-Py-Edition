import net.minecraft.util.logger.Logger as logger
from net.minecraft.world.block import Block
import net.minecraft.modloader.core.registry.BuiltInRegistries as BuiltInRegistries
from net.minecraft.entity.PigEntity import PigEntity

modid="examplemod"

def onStartup(eventBus):
	logger.info("Loading example mod", modid)
	eventBus.register(BuiltInRegistries.BLOCK, modid, "example_block", Block)
	eventBus.register(BuiltInRegistries.ITEM, modid, "example_item")
	eventBus.register(BuiltInRegistries.ENTITY, modid, "example_pig", PigEntity)
