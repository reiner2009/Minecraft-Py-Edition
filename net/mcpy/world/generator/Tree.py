import net.mcpy.world.block.Blocks as Blocks

class Tree:
	def __init__(self, rng):
		self.tree={}
		self.treeH=rng.randint(0, 3)+4
		for x in range(-2, 3):
			for y in range(self.treeH-3, self.treeH-1):
				for z in range(-2, 3):
					self.tree[(x,y,z)]=Blocks.OAK_LEAVES
		for y in range(self.treeH):
			self.tree[(0,y,0)]=Blocks.OAK_LOG
		self.tree[(0,self.treeH, 0)]=Blocks.OAK_LEAVES
		self.tree[(1,self.treeH, 0)]=Blocks.OAK_LEAVES
		self.tree[(-1,self.treeH, 0)]=Blocks.OAK_LEAVES
		self.tree[(0,self.treeH, 1)]=Blocks.OAK_LEAVES
		self.tree[(0,self.treeH, -1)]=Blocks.OAK_LEAVES
		self.tree[(1,self.treeH-1, 0)]=Blocks.OAK_LEAVES
		self.tree[(-1,self.treeH-1, 0)]=Blocks.OAK_LEAVES
		self.tree[(0,self.treeH-1, 1)]=Blocks.OAK_LEAVES
		self.tree[(0,self.treeH-1, -1)]=Blocks.OAK_LEAVES
		if rng.randint(0,10) > 1:
			self.tree.pop((-2, self.treeH-3, -2),None)
			self.tree.pop((-2, self.treeH-2, -2),None)
		if rng.randint(0,20) > 2:
			self.tree.pop((2, self.treeH-3, -2),None)
			self.tree.pop((2, self.treeH-2, -2),None)
		if rng.randint(0,30) > 3:
			self.tree.pop((2, self.treeH-3, 2),None)
			self.tree.pop((2, self.treeH-2, 2),None)
		if rng.randint(0,40) > 4:
			self.tree.pop((-2, self.treeH-3, 2),None)
			self.tree.pop((-2, self.treeH-2, 2),None)
	def place(self, level, feature_x, feature_y, feature_z):
		for (x,y,z) in self.tree.keys():
			level.setBlock(x+feature_x, y+feature_y, z+feature_z, self.tree[(x,y,z)].create(x+feature_x, y+feature_y, z+feature_z))
	def checkSpawnRules(self, level, x, y, z):
		return level.getBlock(x,y,z).id.getAsString()=="minecraft:grass_block"\
		and level.getBlock(x+1, y, z).id.getAsString()=="minecraft:air"\
		and level.getBlock(x-1, y, z).id.getAsString()=="minecraft:air"\
		and level.getBlock(x, y, z+1).id.getAsString()=="minecraft:air"\
		and level.getBlock(x, y, z+1).id.getAsString()=="minecraft:air"
		
