from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class TrapdoorBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.STATE=TrapdoorSetProperty()
        self.FACING="south"
        self.VERTICAL_DIRECTION="down"
    @Override
    def setPropertyByPlayer(self, entity):
        if -90 < entity.get_entity_facing()[1] < 0:
            self.STATE.setState("up")
            self.VERTICAL_DIRECTION="up"
        if 0 < entity.get_entity_facing()[1] < 90:
            self.STATE.setState("down")
            self.VERTICAL_DIRECTION="down"
        self.FACING=entity.get_cardinal_direction_facing()
    @Override
    def onInteraction(self, entity, block_sound_volume):
        if self.STATE.getState()=="up" or self.STATE.getState()=="down":
            self.STATE.setState(self.FACING)
            play_block_sound("oak_trapdoor_open", block_sound_volume)
        else:
            self.STATE.setState(self.VERTICAL_DIRECTION)
            play_block_sound("oak_trapdoor_close", block_sound_volume)
        entity.swing("right")
        super().finallyPlace(entity, 0)
    @Override
    def placeableBlockDuringInteraction(self, entity):
        return False
    @Override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.STATE.getState()
    @Override
    def getDefaultProperty(self):
        return "down"
    @Override
    def getProperties(self):
        return self.STATE.getStateKeys()
    @Override
    def getVoxelShape(self, x, y, z):
        self.VOXEL_SHAPE_MAP={
            "north":[(-1, -1, -1), (1, -1, -1), (1, -1, -0.625), (-1, -1, -0.625), (-1, 1, -1), (1, 1, -1), (1, 1, -0.625),(-1, 1, -0.625)],
            "south":[(-1, -1, 1), (1, -1, 1), (1, -1, 0.625), (-1, -1, 0.625), (-1, 1, 1), (1, 1, 1), (1, 1, 0.625),(-1, 1, 0.625)],
            "west": [(-0.625, -1, -1), (-1, -1, -1), (-1, -1, 1), (-0.625, -1, 1), (-0.625, 1, -1), (-1, 1, -1), (-1, 1, 1),(-0.625, 1, 1)],
            "east": [(1, -1, -1), (0.625, -1, -1), (0.625, -1, 1), (1, -1, 1), (1, 1, -1), (0.625, 1, -1), (0.625, 1, 1),(1, 1, 1)],
            "up":[(-1, 0.625, -1), (1, 0.625, -1), (1, 0.625, 1), (-1, 0.625, 1), (-1, 1, -1), (1, 1, -1), (1, 1, 1),(-1, 1, 1)],
            "down":[(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (-1, -0.625, -1), (1, -0.625, -1), (1, -0.625, 1),(-1, -0.625, 1)]
        }
        self.VOXEL_SHAPE = self.VOXEL_SHAPE_MAP[self.STATE.getState()]
        return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)
    @Override
    def getCollisionShape(self):
        self.COLLISION_SHAPE_MAP={
            "north":AABB(-0.5, -0.5, -0.5, 0.5, 0.5, -0.3125, *self.MAP_POSITION),
            "east":AABB(0.3125, -0.5, -0.5, 0.5, 0.5, 0.5, *self.MAP_POSITION),
            "west":AABB(-0.5, -0.5, -0.5, -0.3125, 0.5, 0.5, *self.MAP_POSITION),
            "south":AABB(-0.5, -0.5, 0.3125, 0.5, 0.5, 0.5, *self.MAP_POSITION),
            "up":AABB(-0.5, 0.3125, -0.5, 0.5, 0.5, 0.5, *self.MAP_POSITION),
            "down":AABB(-0.5, -0.5, -0.5, 0.5, -0.3125, 0.5, *self.MAP_POSITION)
        }
        return self.COLLISION_SHAPE_MAP[self.STATE.getState()]
