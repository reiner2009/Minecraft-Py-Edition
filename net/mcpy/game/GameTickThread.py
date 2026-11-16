import threading
import time
import net.mcpy.client.input.InputHandler as InputHandler
import net.mcpy.game.Minecraft as Minecraft
import net.mcpy.client.renderer.world.level.LevelRenderer as LevelRenderer
import net.mcpy.client.renderer.world.WorldRenderer as WorldRenderer

entity_movement_tick_mainloop=True
tick_mainloop=True

def tick_entity_movement():
	while entity_movement_tick_mainloop:
		InputHandler.tickPlayerMovement()
		time.sleep(1/60)
		
def tick():
	while tick_mainloop:
		time.sleep(1/20)

def tickClient():
	while tick_mainloop:
			for chunk in Minecraft.level.chunks.values():
				if chunk.dirty:
					WorldRenderer.level_renderer.set_chunk_dirty(chunk)
			time.sleep(1/20)

entity_movement_tick_thread=threading.Thread(target=tick_entity_movement, daemon=True)
tick_thread=threading.Thread(target=tick, daemon=True)
client_tick_thread=threading.Thread(target=tickClient, daemon=True)
