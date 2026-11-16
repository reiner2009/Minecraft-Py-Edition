from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class FallingBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
    @Override
    def update(self):
        from net.minecraft.world.chunk.Chunk import get_block
        if get_block(self.MAP_POSITION[0], self.MAP_POSITION[1]-1,self.MAP_POSITION[2])=="air":
            from net.minecraft.world.entity.Entities import entities
            from net.minecraft.world.chunk.Chunk import set_block
            self.falling_block=entities["falling_"+self.NAME]()
            self.falling_block.spawn(*self.MAP_POSITION)
            set_block(*self.MAP_POSITION, "air")
            reloadChunks()
    @Override
    def onPlace(self, entity, block_sound_volume):
        self.update()
        super().onPlace(entity, block_sound_volume)
