import net.minecraft.util.Logger as logger
from net.minecraft.world.block import Block
import net.minecraft.modloader.core.registry.BuiltInRegistries as BuiltInRegistries
from net.minecraft.world.entity.PigEntity import PigEntity
from Blocks import CustomBlock

modid="examplemod"

def onStartup(eventBus):
	logger.info("Loading example mod", modid)
	eventBus.register(BuiltInRegistries.BLOCK, modid, "example_block", Block)
	eventBus.register(BuiltInRegistries.ITEM, modid, "example_item")
	eventBus.register(BuiltInRegistries.BLOCK, modid, "custom_block", CustomBlock)
	eventBus.register(BuiltInRegistries.ENTITY, modid, "example_pig", PigEntity)
	eventBus.register(BuiltInRegistries.ITEM_GROUP_ENTRIES, modid, "example_block")
	eventBus.register(BuiltInRegistries.ITEM_GROUP_ENTRIES, modid, "custom_block")
	eventBus.register(BuiltInRegistries.ITEM_GROUP_ENTRIES, modid, "example_item")
