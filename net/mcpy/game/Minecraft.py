import net.mcpy.world.block.Blocks as Blocks
import net.mcpy.world.generator.Features
import net.mcpy.game as game
import net.mcpy.game.GameTickThread as GameTickThread
from net.mcpy.world.level.Level import Level
from net.mcpy.world.generator.WorldGenerator import generateWorld
import random

seed=random.randint(-(2**63), (2**63) - 1)

level=generateWorld(seed)

def init():
	GameTickThread.tick_thread.start()
