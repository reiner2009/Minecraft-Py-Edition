from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class TntBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
    def ignite(self, block_sound_volume, c):
        from net.minecraft.world.entity.Entities import entities
        from net.minecraft.world.chunk.Chunk import set_block
        self.ignited_tnt=entities["ignited_tnt"](c)
        self.ignited_tnt.set_sound_volume(block_sound_volume)
        self.ignited_tnt.spawn(*self.MAP_POSITION)
        set_block(*self.MAP_POSITION, "air")
        reloadChunks()
    @Override
    def onInteraction(self, entity, block_sound_volume):
        if entity.getMainhandItem()=="flint_and_steel":
            play_block_sound("fuse", block_sound_volume)
            self.ignite(block_sound_volume, 5)
        else:
            super().onInteraction(entity, block_sound_volume)
    @Override
    def onExplode(self, v):
        self.ignite(v, 0.2)
