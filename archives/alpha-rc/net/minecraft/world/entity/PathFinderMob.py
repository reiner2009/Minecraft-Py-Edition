from net.minecraft.world.entity.LivingEntity import LivingEntity
import random
import math
import net.minecraft.client.render.Text as text
from net.minecraft.util import Override

def cos(i):
	return(math.cos(math.radians(i)))

def sin(i):
	return(math.sin(math.radians(i)))

class TargetSelector():
	def __init__(self):
		self.goals=[]
	def addBehaviourGoal(self, weight, target, speed):
		self.goals.append((weight, target, speed))

class PathFinderMob(LivingEntity):
	def __init__(self, name_tag_is_visible=True):
		super().__init__(name_tag_is_visible)
		self.targetSelector=TargetSelector()
		self.nextGoal=0
		self.nextRotGoal=0
		self.seachNewGoal=True
		self.distanceToNextYawTarget=0
		self.distanceToNextTarget=0
	@Override
	def tick(self):
		if self.seachNewGoal:
			if random.randint(0,50)==1:
				self.i=random.randint(0,1)
				self.seachNewGoal=False
				if self.i == 1:
					self.nextGoal=random.randint(1,6)
					self.distanceToNextTarget=0
				if self.i == 0:
					self.nextRotGoal=random.randint(0,180)
					self.distanceToNextYawTarget=0
		else:
			if self.nextGoal > self.distanceToNextTarget:
				self.move(sin(self.yaw)/50,0,cos(self.yaw)/50)
				self.distanceToNextTarget+=1/50
				if self.distanceToNextTarget >= self.nextGoal:
					self.seachNewGoal=True
			elif self.nextRotGoal > self.distanceToNextYawTarget:
				self.rotate(10, 0)
				self.distanceToNextYawTarget+=10
				if self.distanceToNextYawTarget >= self.nextRotGoal:
					self.seachNewGoal=True
		text.render_text_billboard(str(self.seachNewGoal), self.x*2,self.y*2+2,self.z*2,0.5,0.3)
