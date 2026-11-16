import net.mcpy.world.block.Blocks as Blocks
import net.mcpy.game as game
import net.mcpy.game.GameTickThread as GameTickThread
from net.mcpy.world.level.Level import Level
from net.mcpy.world.generator.WorldGenerator import generateWorld

level=generateWorld(0)

def init():
	GameTickThread.tick_thread.start()
