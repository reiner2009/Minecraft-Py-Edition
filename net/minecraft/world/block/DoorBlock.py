from net.minecraft.world.block import*
from net.minecraft.world.block.Block import Block

class DoorBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.up_nighbour=None
        self.down_nighbour=None
        self.DIRECTION=DoorSetProperty()
        self.STATE="closed"
        self.VERTICAL_DIRECTION="0"
        self.opening_keys={
            "east":"south",
            "south":"west",
            "west":"north",
            "north":"east"
        }
        self.closing_keys={
            "south":"east",
            "west":"south",
            "north":"west",
            "east":"north"
        }
    @Override
    def setProperty(self, property):
        self.DIRECTION.setDirection(property)
    @Override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.DIRECTION.getDirection()
    @Override
    def setPropertyByPlayer(self, entity):
        from net.minecraft.world.chunk.Chunk import get_block
        if get_block(self.MAP_POSITION[0],self.MAP_POSITION[1]-1,self.MAP_POSITION[2])=="oak_door":
            self.VERTICAL_DIRECTION="0"
        self.DIRECTION.setDirection(entity.get_cardinal_direction_facing()+self.VERTICAL_DIRECTION)
    @Override
    def getDefaultProperty(self):
        return "south0"
    @Override
    def getProperties(self):
        return self.DIRECTION.getDirectionKeys()
    def setVerticalDirection(self, direction):
        self.VERTICAL_DIRECTION=direction
    def getVerticalDirection(self):
        return self.VERTICAL_DIRECTION
    def setState(self, state):
        self.STATE=state
    @Override
    def onPlace(self, entity, block_sound_volume):
        self.up_nighbour = self.MAP_POSITION[0], self.MAP_POSITION[1] + 1, self.MAP_POSITION[2]
        self.down_nighbour = self.MAP_POSITION[0], self.MAP_POSITION[1] - 1, self.MAP_POSITION[2]
        from net.minecraft.world.chunk.Chunk import set_block, get_block, get_block_data
        if get_block(*self.up_nighbour)=="air":
            set_block(*self.up_nighbour, "oak_door")
            get_block_data(*self.up_nighbour).setProperty(self.DIRECTION.getDirection()[:-1]+"1")
            get_block_data(*self.up_nighbour).setVerticalDirection("1")
            super().finallyPlace(entity, block_sound_volume)
        else:
            set_block(*self.MAP_POSITION, "air")
    def breakOtherDoor(self):
        self.up_nighbour = self.MAP_POSITION[0], self.MAP_POSITION[1] + 1, self.MAP_POSITION[2]
        self.down_nighbour = self.MAP_POSITION[0], self.MAP_POSITION[1] - 1, self.MAP_POSITION[2]
        from net.minecraft.world.chunk.Chunk import set_block, get_block_data, get_block
        if get_block(*self.up_nighbour)=="oak_door":
            if get_block_data(*self.up_nighbour).getVerticalDirection()=="1":
                set_block(*self.up_nighbour, "air")
        if get_block(*self.down_nighbour) == "oak_door":
            if get_block_data(*self.down_nighbour).getVerticalDirection()=="0":
                set_block(*self.down_nighbour, "air")
    @Override
    def onBreak(self, entity):
        self.breakOtherDoor()
    @Override
    def getVoxelShape(self, x, y, z):
        self.VOXEL_SHAPE_MAP={
            "south0":[(-1, -1, -1), (1, -1, -1), (1, -1, -0.625), (-1, -1, -0.625), (-1, 3, -1), (1, 3, -1), (1, 3, -0.625),(-1, 3, -0.625)],
            "north0":[(-1, -1, 1), (1, -1, 1), (1, -1, 0.625), (-1, -1, 0.625), (-1, 3, 1), (1, 3, 1), (1, 3, 0.625),(-1, 3, 0.625)],
            "east0": [(-0.625, -1, -1), (-1, -1, -1), (-1, -1, 1), (-0.625, -1, 1), (-0.625, 3, -1), (-1, 3, -1), (-1, 3, 1),(-0.625, 3, 1)],
            "west0": [(1, -1, -1), (0.625, -1, -1), (0.625, -1, 1), (1, -1, 1), (1, 3, -1), (0.625, 3, -1), (0.625, 3, 1),(1, 3, 1)],
            "south1": [(-1, -3, -1), (1, -3, -1), (1, -3, -0.625), (-1, -3, -0.625), (-1, 1, -1), (1, 1, -1),(1, 1, -0.625), (-1, 1, -0.625)],
            "north1": [(-1, -3, 1), (1, -3, 1), (1, -3, 0.625), (-1, -3, 0.625), (-1, 1, 1), (1, 1, 1), (1, 1, 0.625),(-1, 1, 0.625)],
            "east1": [(-0.625, -3, -1), (-1, -3, -1), (-1, -3, 1), (-0.625, -3, 1), (-0.625, 1, -1), (-1, 1, -1), (-1, 1, 1), (-0.625, 1, 1)],
            "west1": [(1, -3, -1), (0.625, -3, -1), (0.625, -3, 1), (1, -3, 1), (1, 1, -1), (0.625, 1, -1),(0.625, 1, 1), (1, 1, 1)],
        }
        self.VOXEL_SHAPE = self.VOXEL_SHAPE_MAP[self.DIRECTION.getDirection()]
        return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)
    @Override
    def onInteraction(self, entity, block_sound_volume):
        self.up_nighbour = self.MAP_POSITION[0], self.MAP_POSITION[1] + 1, self.MAP_POSITION[2]
        self.down_nighbour = self.MAP_POSITION[0], self.MAP_POSITION[1] - 1, self.MAP_POSITION[2]
        from net.minecraft.world.chunk.Chunk import get_block_data
        if self.STATE=="closed":
            self.STATE="open"
            self.DIRECTION.setDirection(self.opening_keys[self.DIRECTION.getDirection()[:-1]]+self.VERTICAL_DIRECTION)
            if self.VERTICAL_DIRECTION=="0":
                get_block_data(*self.up_nighbour).setProperty(self.DIRECTION.getDirection()[:-1]+"1")
                get_block_data(*self.up_nighbour).setState(self.STATE)
            elif self.VERTICAL_DIRECTION=="1":
                get_block_data(*self.down_nighbour).setProperty(self.DIRECTION.getDirection()[:-1]+"0")
                get_block_data(*self.down_nighbour).setState(self.STATE)
            play_block_sound("oak_door_open", block_sound_volume)
        elif self.STATE=="open":
            self.STATE="closed"
            self.DIRECTION.setDirection(self.closing_keys[self.DIRECTION.getDirection()[:-1]]+self.VERTICAL_DIRECTION)
            if self.VERTICAL_DIRECTION=="0":
                get_block_data(*self.up_nighbour).setProperty(self.DIRECTION.getDirection()[:-1]+"1")
                get_block_data(*self.up_nighbour).setState(self.STATE)
            elif self.VERTICAL_DIRECTION=="1":
                get_block_data(*self.down_nighbour).setProperty(self.DIRECTION.getDirection()[:-1]+"0")
                get_block_data(*self.down_nighbour).setState(self.STATE)
            play_block_sound("oak_door_close", block_sound_volume)
        entity.swing("right")
        super().finallyPlace(entity, 0)
    @Override
    def onExplode(self, v):
        self.breakOtherDoor()
        super().onExplode(v)
    @Override
    def placeableBlockDuringInteraction(self, entity):
        return False
    @Override
    def getCollisionShape(self):
        self.COLLISION_SHAPE_MAP={
            "south":AABB(-0.5, -0.5, -0.5, 0.5, 0.5, -0.3125, *self.MAP_POSITION),
            "west":AABB(0.3125, -0.5, -0.5, 0.5, 0.5, 0.5, *self.MAP_POSITION),
            "east":AABB(-0.5, -0.5, -0.5, -0.3125, 0.5, 0.5, *self.MAP_POSITION),
            "north":AABB(-0.5, -0.5, 0.3125, 0.5, 0.5, 0.5, *self.MAP_POSITION)
        }
        return self.COLLISION_SHAPE_MAP[self.DIRECTION.getDirection()[:-1]]
