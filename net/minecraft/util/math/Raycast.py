from net.minecraft.world.chunk.Chunk import get_block, get_block_data
from net.minecraft.world.phys import AABB
import math
import threading
import time

def get_look_direction(ran, entity):
	world_x, world_y, world_z=entity.get_entity_position()
	yaw, pitch = entity.get_entity_facing()
	dx=world_x+(math.sin(math.radians(yaw))*math.cos(math.radians(pitch)))*ran
	dy=world_y-(math.sin(math.radians(pitch)))*ran
	dz=world_z-(math.cos(math.radians(yaw))*math.cos(math.radians(pitch)))*ran
	return dx ,dy, dz

def get_look_direction_as_d(entity):
	yaw, pitch = entity.get_entity_facing()
	dx=(math.sin(math.radians(yaw))*math.cos(math.radians(pitch)))
	dy=-(math.sin(math.radians(pitch)))
	dz=-(math.cos(math.radians(yaw))*math.cos(math.radians(pitch)))
	return dx ,dy, dz

def get_tracked_pos(entity):
	t=0
	px,py,pz=None, None, None
	startx,starty,startz=entity.get_entity_position()
	bx=round(startx)
	by=round(starty)
	bz=round(startz)
	x,y,z=startx,starty,startz

	dx,dy,dz=get_look_direction_as_d(entity)

	# DDA-Zellen entsprechen dem bestehenden round()-System.
	# Die Grenzen liegen deshalb bei x/y/z = n + 0.5.

	# aktueller Block
	cx=round(startx)
	cy=round(starty)
	cz=round(startz)

	# X
	if dx > 0:
		next_x=cx+0.5
		tMaxX=(next_x-startx)/dx
		tDeltaX=1.0/dx
	elif dx < 0:
		next_x=cx-0.5
		tMaxX=(next_x-startx)/dx
		tDeltaX=-1.0/dx
	else:
		tMaxX=float("inf")
		tDeltaX=float("inf")

	# Y
	if dy > 0:
		next_y=cy+0.5
		tMaxY=(next_y-starty)/dy
		tDeltaY=1.0/dy
	elif dy < 0:
		next_y=cy-0.5
		tMaxY=(next_y-starty)/dy
		tDeltaY=-1.0/dy
	else:
		tMaxY=float("inf")
		tDeltaY=float("inf")

	# Z
	if dz > 0:
		next_z=cz+0.5
		tMaxZ=(next_z-startz)/dz
		tDeltaZ=1.0/dz
	elif dz < 0:
		next_z=cz-0.5
		tMaxZ=(next_z-startz)/dz
		tDeltaZ=-1.0/dz
	else:
		tMaxZ=float("inf")
		tDeltaZ=float("inf")

	while t <= 5:

		# Mittelpunkt/aktuellen Punkt des Rays bestimmen
		x,y,z=get_look_direction(t, entity)

		block=get_block(cx,cy,cz)

		if block!="air":

			voxelShape=get_block_data(cx,cy,cz).getVoxelShape()

			# Ray gegen die VoxelShape prüfen.
			# Gleiche Intersections-Logik wie später in deinem Originalcode.
			minx=voxelShape.minX
			miny=voxelShape.minY
			minz=voxelShape.minZ
			maxx=voxelShape.maxX
			maxy=voxelShape.maxY
			maxz=voxelShape.maxZ

			if dx != 0:
				tx1=(minx-startx)/dx
				tx2=(maxx-startx)/dx
			else:
				tx1=-float("inf")
				tx2=float("inf")

			if dy != 0:
				ty1=(miny-starty)/dy
				ty2=(maxy-starty)/dy
			else:
				ty1=-float("inf")
				ty2=float("inf")

			if dz != 0:
				tz1=(minz-startz)/dz
				tz2=(maxz-startz)/dz
			else:
				tz1=-float("inf")
				tz2=float("inf")

			tx_min=min(tx1,tx2)
			tx_max=max(tx1,tx2)
			ty_min=min(ty1,ty2)
			ty_max=max(ty1,ty2)
			tz_min=min(tz1,tz2)
			tz_max=max(tz1,tz2)

			t_enter=max(tx_min,ty_min,tz_min)
			t_exit=min(tx_max,ty_max,tz_max)

			# Der Treffer muss innerhalb des aktuell durchlaufenen
			# DDA-Blocks liegen.
			next_t=min(tMaxX,tMaxY,tMaxZ)

			if t_enter <= t_exit and t_exit >= t and t_enter <= next_t and t_exit >= 0:
				x,y,z=get_look_direction(max(t,t_enter), entity)

				if AABB(x,y,z,x,y,z).intersects(voxelShape):
					bx=cx
					by=cy
					bz=cz
					t=max(t,t_enter)
					break

		# Nächste DDA-Grenze
		if tMaxX <= tMaxY and tMaxX <= tMaxZ:
			t=tMaxX
			tMaxX+=tDeltaX
			if dx > 0:
				cx+=1
			else:
				cx-=1

		elif tMaxY <= tMaxX and tMaxY <= tMaxZ:
			t=tMaxY
			tMaxY+=tDeltaY
			if dy > 0:
				cy+=1
			else:
				cy-=1

		else:
			t=tMaxZ
			tMaxZ+=tDeltaZ
			if dz > 0:
				cz+=1
			else:
				cz-=1

	if get_block(round(x),round(y),round(z))!="air":
		voxelShape=get_block_data(round(x),round(y),round(z)).getVoxelShape()
		bx=round(x)
		by=round(y)
		bz=round(z)
		minx=voxelShape.minX
		miny=voxelShape.minY
		minz=voxelShape.minZ
		maxx=voxelShape.maxX
		maxy=voxelShape.maxY
		maxz=voxelShape.maxZ
		dx,dy,dz=get_look_direction_as_d(entity)
		if dx != 0:
			tx1 = (minx - startx) / dx
			tx2 = (maxx - startx) / dx
		else:
			tx1 = -float("inf")
			tx2 = float("inf")
		if dy != 0:
			ty1 = (miny - starty) / dy
			ty2 = (maxy - starty) / dy
		else:
			ty1 = -float("inf")
			ty2 = float("inf")
		if dz != 0:
			tz1 = (minz - startz) / dz
			tz2 = (maxz - startz) / dz
		else:
			tz1 = -float("inf")
			tz2 = float("inf")
		tx_min = min(tx1, tx2)
		tx_max = max(tx1, tx2)
		ty_min = min(ty1, ty2)
		ty_max = max(ty1, ty2)
		tz_min = min(tz1, tz2)
		tz_max = max(tz1, tz2)
		t_enter = max(tx_min, ty_min, tz_min)
		if t_enter == tx_min and dx != 0:
			if tx1 < tx2:
				px, py, pz = bx - 1, by, bz
			else:
				px, py, pz = bx + 1, by, bz
		elif t_enter == ty_min and dy != 0:
			if ty1 < ty2:
				px, py, pz = bx, by - 1, bz
			else:
				px, py, pz = bx, by + 1, bz
		elif t_enter == tz_min and dz != 0:
			if tz1 < tz2:
				px, py, pz = bx, by, bz - 1
			else:
				px, py, pz = bx, by, bz + 1

	if px is not None and py is not None and pz is not None:
		if get_block(px, py, pz)=="air":
			return px,py,pz,bx,by,bz
	return None,None,None,bx,by,bz

class RaycastThread:
	def __init__(self, entity):
		self.entity=entity
		self.running=False
		self.px=None
		self.py=None
		self.pz=None
		self.bx=None
		self.by=None
		self.bz=None
	def run(self):
		while self.running:
			self.px, self.py, self.pz, self.bx, self.by, self.bz=get_tracked_pos(self.entity)
			time.sleep(0.03)
	def start(self):
		self.running=True
		self.thread=threading.Thread(target=self.run, daemon=True)
		self.thread.start()
	def get_pos(self):
		return self.px,self.py,self.pz,self.bx,self.by,self.bz

raycastThread=None

def setRaycastThread(entity):
	global raycastThread
	raycastThread=RaycastThread(entity)
	raycastThread.start()

def get_pos(entity):
	return raycastThread.get_pos()