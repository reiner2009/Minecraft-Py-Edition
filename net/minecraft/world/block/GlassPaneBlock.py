from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class GlassPaneBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.DIRECTION=TwoDirectionsProperty("x")
    @Override
    def setPropertyByPlayer(self, entity):
        if entity.get_cardinal_direction_facing() == "south" or entity.get_cardinal_direction_facing() == "north":
            self.DIRECTION.setDirection("z")
        elif entity.get_cardinal_direction_facing() == "west" or entity.get_cardinal_direction_facing() == "east":
            self.DIRECTION.setDirection("x")
    @Override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.DIRECTION.getDirection()
    @Override
    def getDefaultProperty(self):
        return "x"
    @Override
    def getProperties(self):
        return self.DIRECTION.getDirectionKeys()
    @Override
    def getVoxelShape(self, x, y, z):
        if self.DIRECTION.getDirection()=="x":
            self.VOXEL_SHAPE = [(-0.125, -1, -1), (0.125, -1, -1), (0.125, -1, 1), (-0.125, -1, 1), (-0.125, 1, -1), (0.125, 1, -1), (0.125, 1, 1),(-0.125, 1, 1)]
        if self.DIRECTION.getDirection()=="z":
            self.VOXEL_SHAPE = [(-1, -1, -0.125), (1, -1, -0.125), (1, -1, 0.125), (-1, -1, 0.125), (-1, 1, -0.125), (1, 1, -0.125), (1, 1, 0.125), (-1, 1, 0.125)]
        return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)
    @Override
    def getCollisionShape(self):
        if self.DIRECTION.getDirection()=="x":
            return AABB(-0.0625, -0.5, -0.5, 0.0625, 0.5,0.5, *self.MAP_POSITION)
        if self.DIRECTION.getDirection()=="z":
            return AABB(-0.5, -0.5, -0.0625, 0.5, 0.5, 0.0625, *self.MAP_POSITION)
