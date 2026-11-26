from net.mcpy.world.chunk.Chunk import Chunk
import net.mcpy.world.block.Blocks as Blocks
import threading

class Level:
	def __init__(self):
		self.chunks={}
		self.lock=threading.Lock()
	def setBlock(self,x,y,z,block, update=True):
		with self.lock:
			chunk_x, chunk_z=Chunk.parseBlockPos(x,y,z)
			local_x=x % 8
			local_z=z % 8
			chunk_key=(chunk_x, chunk_z)
			if chunk_key not in self.chunks:
				self.chunks[chunk_key]=Chunk(chunk_x, chunk_z)
			self.chunks[chunk_key].setBlock(local_x, y, local_z, block, update)
			if update:
				if local_x==0:
					try:
						self.chunks[(chunk_x - 1, chunk_z)].dirty=True
					except KeyError:
						pass
				if local_x==7:
					try:
						self.chunks[(chunk_x + 1, chunk_z)].dirty=True
					except KeyError:
						pass
				if local_z==0:
					try:
						self.chunks[(chunk_x, chunk_z - 1)].dirty=True
					except KeyError:
						pass
				if local_z==7:
					try:
						self.chunks[(chunk_x, chunk_z + 1)].dirty=True
					except KeyError:
						pass
	def getBlock(self,x,y,z):
		chunk_x, chunk_z=Chunk.parseBlockPos(x,y,z)
		local_x=x % 8
		local_z=z % 8
		chunk=self.chunks.get((chunk_x, chunk_z))
		if chunk is None:
			return Blocks.VOID.create(x,y,z)
		return chunk.getBlock(local_x, y, local_z)
					
