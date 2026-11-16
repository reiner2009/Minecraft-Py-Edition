from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class LeavesBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
    @Override
    def hasCollision(self):
        return False
