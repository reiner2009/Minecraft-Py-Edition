from net.minecraft.world.EntityList import entity_chunk

class Entity:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0
		self.yaw = 90
		self.pitch = 0
		self.name="Entity"
		self.movement=False
		self.thirt_person_perspective = 0
		entity_chunk.append(self)
	def spawn(self, x, y, z, yaw=90, pitch=0):
		self.x = x
		self.y = y
		self.z = z
		self.yaw = yaw
		self.pitch = pitch
	def rotate(self, yaw_change, pitch_change):
		self.yaw = (self.yaw + yaw_change)
		self.yaw = ((self.yaw + 180) % 360) - 180
		self.pitch = self.pitch - pitch_change
		self.pitch=max(-90, min(90, self.pitch))
	def get_entity_facing(self):
		return self.yaw, self.pitch
	def get_cardinal_direction_facing(self):
		yaw = self.get_entity_facing()[0]
		if -45 <= yaw <= 45:
			return "north"
		elif 45 < yaw <= 135:
			return "east"
		elif yaw > 135 or yaw <= -135:
			return "south"
		elif -135 < yaw <= -45:
			return "west"
	def set_facing(self, yaw, pitch):
		self.yaw = yaw
		self.pitch = pitch
	def setName(self, name):
		self.name = name
	def move(self, x,y,z):
		self.x += x
		self.y += y
		self.z += z
	def get_entity_position(self):
		return self.x, self.y, self.z
	def set_thirt_person_perspective(self):
		self.thirt_person_perspective+=1
		if self.thirt_person_perspective >= 3:
			self.thirt_person_perspective = 0
	def get_thirt_person_perspective(self):
		return self.thirt_person_perspective
	def tick(self):
		pass
	def discard(self):
		entity_chunk.remove(self)
	
