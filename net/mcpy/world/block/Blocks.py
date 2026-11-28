import net.mcpy.registry.Registry as Registry
import net.mcpy.registry.Registries as Registries
from net.mcpy.resources.Identifier import Identifier
from net.mcpy.world.block.AxisBlock import AxisBlock
from net.mcpy.world.block.Block import Block


def registerBlock(block):
	Registry.register(Registries.BLOCK, block.id, block)
	return block

AIR=registerBlock(Block(Identifier(path="air")))
VOID=registerBlock(Block(Identifier(path="void")))
BEDROCK=registerBlock(Block(Identifier(path="bedrock")))
DEPPSLATE=registerBlock(AxisBlock(Identifier(path="deepslate")))
STONE=registerBlock(Block(Identifier(path="stone")))
DIRT=registerBlock(Block(Identifier(path="dirt")))
GRASS_BLOCK=registerBlock(Block(Identifier(path="grass_block")))
OAK_LEAVES=registerBlock(Block(Identifier(path="oak_leaves")))
OAK_LOG=registerBlock(AxisBlock(Identifier(path="oak_log")))
BLUE_STAINED_GLASS_BLOCK=registerBlock(Block(Identifier(path="blue_stained_glass_block")))
STONE_BRICKS=registerBlock(Block(Identifier(path="stone_bricks")))
GLASS_BLOCK=registerBlock(Block(Identifier(path="glass_block")))
OAK_PLANKS=registerBlock(Block(Identifier(path="oak_planks")))

ready=False

def init():
	global ready
	ready=True
	
