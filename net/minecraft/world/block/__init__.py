from typing import override

from net.minecraft.world.block.props import AxisProperty, FacingProperty

class Block:
    def __init__(self, NAME):
        self.VOXEL_SHAPE=[1,1,1]
        self.COLLISION_SHAPE=[1,1,1]
        self.NAME = NAME
        self.MAP_POSITION = (0,0,0)
    def setPos(self, x, y,z):
        self.MAP_POSITION = (x,y,z)
    def getCollisionShape(self):
        return self.COLLISION_SHAPE
    def getVoxelShape(self):
        return self.VOXEL_SHAPE
    def getName(self):
        return self.NAME
    def getProperty(self):
        return ""
    def getDefaultProperty(self):
        return ""
    def finallyPlace(self, entity):
        pass
    def getProperties(self):
        return [""]

class LogBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.AXIS=AxisProperty("y")
    @override
    def finallyPlace(self, entity):
        if -45<entity.get_entity_facing()[1]<0 or 0<entity.get_entity_facing()[1]<45:
            if entity.get_cardinal_direction_facing()=="south" or entity.get_cardinal_direction_facing()=="north":
                self.AXIS.setAxis("z")
            elif entity.get_cardinal_direction_facing()=="west" or entity.get_cardinal_direction_facing()=="east":
                self.AXIS.setAxis("x")
        else:
            self.AXIS.setAxis("y")
    @override
    def getProperty(self):
        return self.AXIS.getAxis()
    @override
    def getDefaultProperty(self):
        return "y"
    @override
    def getProperties(self):
        return self.AXIS.getAxisKeys()

class FurnaceBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.FACING=FacingProperty()
    @override
    def finallyPlace(self, entity):
        if entity.get_cardinal_direction_facing()=="north":
            self.FACING.setFacing("north")
        if entity.get_cardinal_direction_facing()=="south":
            self.FACING.setFacing("south")
        if entity.get_cardinal_direction_facing()=="east":
            self.FACING.setFacing("east")
        if entity.get_cardinal_direction_facing()=="west":
            self.FACING.setFacing("west")
    @override
    def getProperty(self):
        return self.FACING.getFacing()
    @override
    def getDefaultProperty(self):
        return "south"
    @override
    def getProperties(self):
        return self.FACING.getFacingKeys()