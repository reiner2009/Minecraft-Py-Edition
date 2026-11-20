from OpenGL.GL import*
import threading
import net.mcpy.client.renderer.world.chunk.ChunkRenderer as ChunkRendererModule
from net.mcpy.client.renderer.world.chunk.ChunkRenderer import ChunkRenderer

def init():
	ChunkRendererModule.init()
	
def updateView():
	ChunkRendererModule.updateView()

class LevelRenderer:
	def __init__(self):
		self.chunk_renderers={}
		self.dirty_chunks={}
		self.lock=threading.Lock()
	def set_chunk_dirty(self, chunk):
		self.dirty_chunks[(chunk.x, chunk.z)]=chunk
	def add_chunk(self, chunk):
		self.chunk_renderer_key=(chunk.x, chunk.z)
		if self.chunk_renderer_key not in self.chunk_renderers:
			self.chunk_renderers[self.chunk_renderer_key]=[ChunkRenderer("solide", chunk), ChunkRenderer("cutout", chunk), ChunkRenderer("translucent", chunk)]
			for chunk_renderer in self.chunk_renderers[(chunk.x, chunk.z)]:
				chunk_renderer.dirty=True
		else:
			for chunk_renderer in self.chunk_renderers[(chunk.x, chunk.z)]:
				chunk_renderer.dirty=True	 
	def render(self):
		with self.lock:
			if self.dirty_chunks:
				for K, chunk in self.dirty_chunks.items():
					self.add_chunk(chunk)
				self.dirty_chunks={}
				from net.mcpy.game import GameTickThread
				GameTickThread.client_tick_event.set()
		for chunk_renderer in self.chunk_renderers.values():
			chunk_renderer[0].render()
		for chunk_renderer in self.chunk_renderers.values():
			chunk_renderer[1].render()
		for chunk_renderer in self.chunk_renderers.values():
			glEnable(GL_BLEND)
			glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
			chunk_renderer[2].render()
			glDisable(GL_BLEND)
