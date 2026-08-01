from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class FenceBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.DIRECTION=FenceState()
    @Override
    def setPropertyByPlayer(self, entity):
        self.x, self.y, self.z = self.MAP_POSITION
        self.neighbours=[(self.x+1, self.y, self.z),(self.x-1, self.y, self.z),(self.x, self.y, self.z+1),(self.x, self.y, self.z-1)]
        from net.minecraft.world.chunk.Chunk import get_block
        if (get_block(*self.neighbours[0])=="oak_fence" or get_block(*self.neighbours[1])=="oak_fence") and (get_block(*self.neighbours[2])=="air" and get_block(*self.neighbours[3])=="air"):
            self.DIRECTION.setDirection("z")
        elif (get_block(*self.neighbours[2])=="oak_fence" or get_block(*self.neighbours[3])=="oak_fence") and (get_block(*self.neighbours[0])=="air" and get_block(*self.neighbours[1])=="air"):
            self.DIRECTION.setDirection("x")
        else:
            self.DIRECTION.setDirection("cross")
    @Override
    def update(self):
        self.setPropertyByPlayer(None)
    @Override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.DIRECTION.getDirection()
    @Override
    def getDefaultProperty(self):
        return "x"
    @Override
    def getProperties(self):
        return self.DIRECTION.getDirectionKeys()
    @Override
    def getVoxelShape(self, x, y, z):
        if self.DIRECTION.getDirection() == "x":
            self.VOXEL_SHAPE = [(-0.25, -1, -1), (0.25, -1, -1), (0.25, -1, 1), (-0.25, -1, 1), (-0.25, 1, -1),(0.25, 1, -1), (0.25, 1, 1), (-0.25, 1, 1)]
            return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)
        if self.DIRECTION.getDirection() == "z":
            self.VOXEL_SHAPE = [(-1, -1, -0.25), (1, -1, -0.25), (1, -1, 0.25), (-1, -1, 0.25), (-1, 1, -0.25),(1, 1, -0.25), (1, 1, 0.25), (-1, 1, 0.25)]
            return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)
        else:
            return super().getVoxelShape(x,y,z)
    @Override
    def getCollisionShape(self):
        self.COLLISIONS_SHAPE_MAP={
            "x": AABB(-0.125, -0.5, -0.5, 0.125, 0.75,0.5, *self.MAP_POSITION),
            "z": AABB(-0.5, -0.5, -0.125, 0.5, 0.75, 0.125, *self.MAP_POSITION),
            "cross": AABB(-0.5, -0.5, -0.5, 0.5, 0.75, 0.5, *self.MAP_POSITION)
        }
        return self.COLLISIONS_SHAPE_MAP[self.DIRECTION.getDirection()]
