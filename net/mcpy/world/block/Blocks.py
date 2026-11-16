import net.mcpy.registry.Registry as Registry
import net.mcpy.registry.Registries as Registries
from net.mcpy.resources.ResourceLocation import ResourceLocation

def registerBlock(name, block=None):
	resource_location=ResourceLocation(path=name)
	Registry.register(Registries.BLOCK, resource_location, block)
	return block

BEDROCK=registerBlock("bedrock")
DEPPSLATE=registerBlock("deepslatey")
STONE=registerBlock("stone")
DIRT=registerBlock("dirt")
GRASS_BLOCK=registerBlock("grass_block")
OAK_LEAVES=registerBlock("oak_leaves")
OAK_LOG=registerBlock("oak_logy")
STONE_BRICKS=registerBlock("blue_stained_glass_block")

ready=False

def init():
	global ready
	ready=True
	
