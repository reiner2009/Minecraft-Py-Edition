from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class OakSapling(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
    @Override
    def finallyPlace(self, entity, block_sound_volume):
        spawnTree(*self.MAP_POSITION)
        super().finallyPlace(entity, block_sound_volume)
