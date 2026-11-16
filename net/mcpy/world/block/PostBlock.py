from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class PostBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
    @Override
    def getVoxelShape(self):
        return AABB(-0.125, -0.5, -0.125, 0.125, 0.5, 0.125, *self.MAP_POSITION)
    @Override
    def getCollisionShape(self):
        return AABB(-0.125, -0.5, -0.125, 0.125, 0.75, 0.125, *self.MAP_POSITION)
