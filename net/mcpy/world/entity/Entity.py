class Entity:
	def __init__(self, x=0, y=0, z=0, pitch=0, yaw=0):
		self.x=x
		self.y=y
		self.z=z
		self.target_x=0
		self.target_y=0
		self.target_z=0
		self.pitch=pitch
		self.yaw=yaw
	def rotate(self, pitch=0, yaw=0):
		self.pitch+=pitch
		self.yaw+=yaw
	def move(self):
		self.x=self.target_x
		self.y=self.target_y
		self.z=self.target_z
	def setDeltaMovement(self, x=0, y=0, z=0):
		self.target_x=self.x+x
		self.target_y=self.y+y
		self.target_z=self.z+z
	def getPos(self):
		return self.x, self.y, self.z
	def spawn(self, x,y,z):
		self.x=x
		self.y=y
		self.z=z
