from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class LogBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.AXIS=AxisProperty("y")
    @Override
    def setPropertyByPlayer(self, entity):
        if -45<entity.get_entity_facing()[1]<0 or 0<entity.get_entity_facing()[1]<45:
            if entity.get_cardinal_direction_facing()=="south" or entity.get_cardinal_direction_facing()=="north":
                self.AXIS.setAxis("z")
            elif entity.get_cardinal_direction_facing()=="west" or entity.get_cardinal_direction_facing()=="east":
                self.AXIS.setAxis("x")
        else:
            self.AXIS.setAxis("y")
    @Override
    def getProperty(self,entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.AXIS.getAxis()
    @Override
    def getDefaultProperty(self):
        return "y"
    @Override
    def getProperties(self):
        return self.AXIS.getAxisKeys()
