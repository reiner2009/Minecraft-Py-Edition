from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class PostBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
    @Override
    def getVoxelShape(self, x, y, z):
        self.VOXEL_SHAPE = [(-0.25, -1, -0.25), (0.25, -1, -0.25), (0.25, -1, 0.25), (-0.25, -1, 0.25), (-0.25, 1, -0.25),(0.25, 1, -0.25), (0.25, 1, 0.25), (-0.25, 1, 0.25)]
        return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)
    @Override
    def getCollisionShape(self):
        return AABB(-0.125, -0.5, -0.125, 0.125, 0.5, 0.125, *self.MAP_POSITION)
