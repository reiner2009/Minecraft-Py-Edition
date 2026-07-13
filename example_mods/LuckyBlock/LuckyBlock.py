from net.minecraft.world.block import Block, spawnTree
from net.minecraft.chat.Chat import show_text
import random

def spawnRandomTree(x,y,z,entity):
	spawnTree(x,y,z)

def teleportPlayer(x,y,z,entity):
	entity.spawn(random.randint(x-5, x+5),random.randint(y-5, y+5),random.randint(z-5, z+5))
	from net.minecraft.world.chunk.Chunk import reload_chunks, set_block
	set_block(x,y,z,"air")
	reload_chunks()

def spawnPigs(x,y,z,entity):
	from net.minecraft.world.entity.Entities import entities
	for i in range(5):
		entities["pig"]().spawn(x,y,z)
	from net.minecraft.world.chunk.Chunk import reload_chunks, set_block
	set_block(x,y,z,"air")
	reload_chunks()

def glassHouse(x,y,z,entity):
	from net.minecraft.world.chunk.Chunk import reload_chunks, set_block
	set_block(x,y,z, "air")
	entity.spawn(round(entity.get_entity_position()[0]),round(entity.get_entity_position()[1]),round(entity.get_entity_position()[2]))
	tx,ty,tz=entity.get_entity_position()
	for X in range(3):
		for Y in range(4):
			for Z in range(3):
				set_block(tx+X-1, ty+Y-2, tz+Z-1, "glass_block")
	set_block(tx, ty, tz, "air")
	set_block(tx,ty-1,tz,"air")
	reload_chunks()

def diamondBlock(x,y,z,entity):
	from net.minecraft.world.chunk.Chunk import reload_chunks, set_block
	set_block(x,y,z, "diamond_block")
	reload_chunks()

def goldBlock(x,y,z,entity):
	from net.minecraft.world.chunk.Chunk import reload_chunks, set_block
	set_block(x,y,z, "gold_block")
	reload_chunks()

def spawnTNT(x,y,z,entity):
	from net.minecraft.world.entity.Entities import entities
	entities["ignited_tnt"]().spawn(x,y,z)
	from net.minecraft.world.chunk.Chunk import reload_chunks, set_block
	set_block(x,y,z,"air")
	reload_chunks()

def sandRain(x,y,z,entity):
	from net.minecraft.world.entity.Entities import entities
	for i in range(5):
		for j in range(5):
			entities["falling_sand"]().spawn(x+i,y+10,z+j)
	from net.minecraft.world.chunk.Chunk import reload_chunks, set_block
	set_block(x,y,z,"air")
	reload_chunks()

def spawn5TNT(x,y,z,entity):
	from net.minecraft.world.entity.Entities import entities
	for i in range(5):
		entities["ignited_tnt"]().spawn(x+i-2,y+2,z)
	from net.minecraft.world.chunk.Chunk import reload_chunks, set_block
	set_block(x,y,z,"air")
	reload_chunks()

def badLuck(x,y,z,entity):
	show_text("Bad luck!!!", [255,0,0,255])
	from net.minecraft.world.chunk.Chunk import reload_chunks, set_block
	set_block(x,y,z,"air")
	reload_chunks()

class LuckyBlock(Block):
	def __init__(self, NAME):
		super().__init__(NAME)
	def placeableBlockDuringInteraction(self, entity):
		return False
	def onInteraction(self, entity, block_sound_volume):
		entity.swing("left")
		entity.swing("right")
		random.choices(list(luckyBlockChanceTable.keys()), weights=luckyBlockChanceTable.values())[0](*self.MAP_POSITION, entity)
		

luckyBlockChanceTable={
	spawnRandomTree:20,
	teleportPlayer:15,
	spawnPigs:15,
	glassHouse:12,
	diamondBlock:10,
	goldBlock:10,
	spawnTNT:8,
	sandRain:5,
	spawn5TNT:3,
	badLuck:2
}