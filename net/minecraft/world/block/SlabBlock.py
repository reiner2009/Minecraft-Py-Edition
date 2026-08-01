from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class SlabBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.VERICAL_POS=SlabSetProperty()
    @Override
    def getProperties(self):
        return self.VERICAL_POS.getVerticalPosKeys()
    @Override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.VERICAL_POS.getVerticalPos()
    @Override
    def setPropertyByPlayer(self, entity):
        if -90 < entity.get_entity_facing()[1] < 0:
            self.VERICAL_POS.setVerticalPos("up")
        if 0 < entity.get_entity_facing()[1] < 90:
            self.VERICAL_POS.setVerticalPos("down")
    @Override
    def getDefaultProperty(self):
        return "down"
    @Override
    def getVoxelShape(self, x, y, z):
        self.VOXEL_SHAPE_MAP = {
            "up": [(-1, 0, -1), (1, 0, -1), (1, 0, 1), (-1, 0, 1), (-1, 1, -1), (1, 1, -1), (1, 1, 1),(-1, 1, 1)],
            "down":[(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (-1, 0, -1), (1, 0, -1), (1, 0, 1),(-1, 0, 1)]
        }
        self.VOXEL_SHAPE = self.VOXEL_SHAPE_MAP[self.VERICAL_POS.getVerticalPos()]
        return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)
    @Override
    def getCollisionShape(self):
        self.COLLISION_SHAPE_MAP={
            "up":AABB(-0.5, 0, -0.5, 0.5, 0.5, 0.5, *self.MAP_POSITION),
            "down":AABB(-0.5, -0.5, -0.5, 0.5, 0, 0.5, *self.MAP_POSITION)
        }
        return self.COLLISION_SHAPE_MAP[self.VERICAL_POS.getVerticalPos()]
