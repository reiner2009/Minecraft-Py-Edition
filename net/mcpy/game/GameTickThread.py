import threading
import time
import net.mcpy.client.input.InputHandler as InputHandler
import net.mcpy.game.Minecraft as Minecraft
import net.mcpy.client.renderer.world.WorldRenderer as WorldRenderer

entity_movement_tick_mainloop=True
tick_mainloop=True

client_tick_event=threading.Event()

def tickEntityMovement():
	while entity_movement_tick_mainloop:
		InputHandler.tickPlayerMovement()
		time.sleep(1/60)
		
def tick():
	while tick_mainloop:
		time.sleep(1/20)

def tickClient():
	while tick_mainloop:
		client_tick_event.wait()
		client_tick_event.clear()
		for chunk in Minecraft.level.chunks.values():
			if chunk.dirty:
				WorldRenderer.level_renderer.set_chunk_dirty(chunk)
				chunk.dirty=False
		with WorldRenderer.level_renderer.lock:
			for chunk_renderers in WorldRenderer.level_renderer.chunk_renderers.values():
				for chunk_renderer in chunk_renderers:
					if chunk_renderer.dirty:
						chunk_renderer.updateVertices()
						chunk_renderer.dirty=False
						chunk_renderer.vbodirty=True

entity_movement_tick_thread=threading.Thread(target=tickEntityMovement, daemon=True)
tick_thread=threading.Thread(target=tick, daemon=True)
client_tick_thread=threading.Thread(target=tickClient, daemon=True)

client_tick_event.set()
