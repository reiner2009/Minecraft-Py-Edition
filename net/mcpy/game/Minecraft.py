import net.mcpy.game.GameTickThread as GameTickThread
from net.mcpy.world.generator.WorldGenerator import generateWorld
import net.mcpy.world.generator.Features as Features
import random

seed=random.randint(-(2**63), (2**63) - 1)

level=generateWorld(seed)

def init():
	GameTickThread.tick_thread.start()
	Features.trigger()
