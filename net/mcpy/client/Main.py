import net.mcpy.client as client
from net.mcpy.world.entity.PlayerEntity import PlayerEntity
import net.mcpy.client.GameClient as GameClient
import net.mcpy.game.GameTickThread as GameTickThread

GameClient.attributes["local_player"]=PlayerEntity(z=-1)

client.init()
GameTickThread.entity_movement_tick_thread.start()
client.render()
client.shutdown()
GameTickThread.entity_movement_tick_mainloop=False
GameTickThread.entity_movement_tick_thread.join()
