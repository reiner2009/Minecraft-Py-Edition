from net.mcpy.world.entity.Entity import Entity
import net.mcpy.world.block.Blocks as Blocks
import math

class PlayerEntity(Entity):
	def __init__(self,x=0,y=0,z=0, yaw=0,pitch=0):
		super().__init__(x,y,z,yaw,pitch)
	def getLookDirection(self, ran):
		dx = self.x + (math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))) * ran
		dy = self.y + (math.sin(math.radians(self.pitch))) * ran
		dz = self.z + (math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))) * ran
		return dx, dy, dz
	def getLookDirectionAsD(self):
		dx = (math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)))
		dy = (math.sin(math.radians(self.pitch)))
		dz = (math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)))
		return dx, dy, dz
	def getTrackedPos(self, level):
		t = 0
		px, py, pz = None, None, None
		startx, starty, startz = self.getPos()
		bx = math.floor(startx)
		by = math.floor(starty)
		bz = math.floor(startz)
		x, y, z = startx, starty, startz
		while t <= 5 and not (level.getBlock(math.floor(x), math.floor(y), math.floor(z)) != Blocks.AIR and level.getBlock(math.floor(x), math.floor(y), math.floor(z)) != Blocks.VOID):
			t += 0.01
			x, y, z = self.getLookDirection(t)
		if level.getBlock(math.floor(x), math.floor(y), math.floor(z)) != Blocks.AIR and level.getBlock(math.floor(x), math.floor(y), math.floor(z)) != Blocks.VOID:
			bx = math.floor(x)
			by = math.floor(y)
			bz = math.floor(z)
			minx = bx
			miny = by
			minz = bz
			maxx = bx + 1
			maxy = by + 1
			maxz = bz + 1
			dx, dy, dz = self.getLookDirectionAsD()
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
			if level.getBlock(math.floor(x), math.floor(y), math.floor(z)) != Blocks.AIR and level.getBlock(math.floor(x), math.floor(y), math.floor(z)) != Blocks.VOID:
				return px, py, pz, bx, by, bz
		return None, None, None, bx, by, bz
