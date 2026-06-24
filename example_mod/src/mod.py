import net.minecraft.util.logger.Logger as logger
from Blocks import CustomBlock
from net.minecraft.world.block import Block
import net.minecraft.modloader.core.registry.BuiltInRegistries as BuiltInRegistries

modid="examplemod"

def onStartup(eventBus):
	logger.info("Loading example mod", modid)
	eventBus.register(BuiltInRegistries.BLOCK, modid, "exampleblock", Block)
	eventBus.register(BuiltInRegistries.BLOCK, modid, "custom_block", CustomBlock)
