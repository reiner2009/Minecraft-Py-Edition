from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class StairBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.STAIR_SET=StairSetProperty("south0")
        self.VERTICAL_DIRECTION="0"
    @Override
    def setPropertyByPlayer(self, entity):
        if -90 < entity.get_entity_facing()[1] < 0:
            self.VERTICAL_DIRECTION="1"
        if 0 < entity.get_entity_facing()[1] < 90:
            self.VERTICAL_DIRECTION="0"
        self.STAIR_SET.setStairSet(entity.get_cardinal_direction_facing()+self.VERTICAL_DIRECTION)
    @Override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.STAIR_SET.getStairSet()
    @Override
    def getDefaultProperty(self):
        return "south0"
    @Override
    def getProperties(self):
        return self.STAIR_SET.getStairSetKeys()
