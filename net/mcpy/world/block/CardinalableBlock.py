from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class CardinalableBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.FACING=FacingProperty()
    @Override
    def setPropertyByPlayer(self, entity):
        self.FACING.setFacing(entity.get_cardinal_direction_facing())
    @Override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.FACING.getFacing()
    @Override
    def getDefaultProperty(self):
        return "south"
    @Override
    def getProperties(self):
        return self.FACING.getFacingKeys()
