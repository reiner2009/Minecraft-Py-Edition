from net.mcpy.world.block.Block import Block

class AxisBlock(Block):
	def __init__(self, id):
		super().__init__(id)
		self.state_id = "axis"
		self.block_state = {"axis": "y", "all": ["x", "y", "z"]}
	def onPlace(self, px,py,pz,bx,by,bz):
		if px!=bx:
			self.setState("axis", "x")
		if py!=by:
			self.setState("axis", "y")
		if pz!=bz:
			self.setState("axis", "z")
