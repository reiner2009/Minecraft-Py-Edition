from net.minecraft.world.block.Block import Block

class CardinalableBlock(Block):
    def __init__(self, id):
        super().__init__(id)
        self.FACING=FacingProperty()
