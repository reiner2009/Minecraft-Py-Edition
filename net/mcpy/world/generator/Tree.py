from net.mcpy.resources.ResourceLocation import ResourceLocation
import random

class Tree:
	def __init__(self):
		oak_log=ResourceLocation(path="oak_logy")
		oak_leaves=ResourceLocation(path="oak_leaves")
		self.tree={}
		self.treeH=random.randint(0, 3)+4
		for x in range(-2, 3):
			for y in range(self.treeH-3, self.treeH-1):
				for z in range(-2, 3):
					self.tree[(x,y,z)]=oak_leaves
		for y in range(self.treeH):
			self.tree[(0,y,0)]=oak_log
		self.tree[(0,self.treeH, 0)]=oak_leaves
		self.tree[(1,self.treeH, 0)]=oak_leaves
		self.tree[(-1,self.treeH, 0)]=oak_leaves
		self.tree[(0,self.treeH, 1)]=oak_leaves
		self.tree[(0,self.treeH, -1)]=oak_leaves
		self.tree[(1,self.treeH-1, 0)]=oak_leaves
		self.tree[(-1,self.treeH-1, 0)]=oak_leaves
		self.tree[(0,self.treeH-1, 1)]=oak_leaves
		self.tree[(0,self.treeH-1, -1)]=oak_leaves
		if random.randint(0,10) > 1:
			self.tree.pop((-2, self.treeH-3, -2),None)
			self.tree.pop((-2, self.treeH-2, -2),None)
		if random.randint(0,10) > 1:
			self.tree.pop((-2, self.treeH-3, -2),None)
			self.tree.pop((2, self.treeH-2, -2),None)
		if random.randint(0,10) > 1:
			self.tree.pop((2, self.treeH-3, -2),None)
			self.tree.pop((-2, self.treeH-2, -2),None)
		if random.randint(0,10) > 1:
			self.tree.pop((2, self.treeH-3, -2),None)
			self.tree.pop((2, self.treeH-2, -2),None)
	def place(self, level, feature_x, feature_y, feature_z):
		for (x,y,z) in self.tree.keys():
			level.setBlock(x+feature_x, y+feature_y, z+feature_z, self.tree[(x,y,z)])
	def checkSpawnRules(self, level, x, y, z):
		return level.getBlock(x,y,z).getAsString()=="minecraft:grass_block"\
		and level.getBlock(x+1, y, z).getAsString()=="minecraft:air"\
		and level.getBlock(x-1, y, z).getAsString()=="minecraft:air"\
		and level.getBlock(x, y, z+1).getAsString()=="minecraft:air"\
		and level.getBlock(x, y, z+1).getAsString()=="minecraft:air"
		
