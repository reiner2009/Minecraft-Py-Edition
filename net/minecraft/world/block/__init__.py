from typing import override


from net.minecraft.world.block.props import AxisProperty, FacingProperty, TwoDirectionsProperty
import net.minecraft.world.Features as features
import net.minecraft.resources.DataLocation as DataLocation
import random
import pickle
import gzip

def spawnTree(x,y,z):
    from net.minecraft.world.chunk.Chunk import set_block, reload_chunks
    tree_percent_map = features.get_feature_list("tree")
    feature = random.choices(list(tree_percent_map.keys()), weights=tree_percent_map.values())[0]
    with gzip.open(DataLocation.get_resource_path("data/minecraft/worldgen/feature/tree/" + feature + ".dat"), "rb") as file:
        tree = pickle.load(file)
    for pos, block in tree.items():
        set_block(x+pos[0],y+pos[1],z+pos[2], block.getName())
    reload_chunks()

def reloadChunks():
    from net.minecraft.world.chunk.Chunk import reload_chunks
    reload_chunks()

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
        reloadChunks()
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
        super().finallyPlace(entity)
    @override
    def getProperty(self):
        return self.AXIS.getAxis()
    @override
    def getDefaultProperty(self):
        return "y"
    @override
    def getProperties(self):
        return self.AXIS.getAxisKeys()

class CardinalableBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.FACING=FacingProperty()
    @override
    def finallyPlace(self, entity):
        self.FACING.setFacing(entity.get_cardinal_direction_facing())
        super().finallyPlace(entity)
    @override
    def getProperty(self):
        return self.FACING.getFacing()
    @override
    def getDefaultProperty(self):
        return "south"
    @override
    def getProperties(self):
        return self.FACING.getFacingKeys()

class OakSapling(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
    @override
    def finallyPlace(self, entity):
        spawnTree(*self.MAP_POSITION)
        super().finallyPlace(entity)

class GlassPane(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.DIRECTION=TwoDirectionsProperty("x")
    @override
    def finallyPlace(self, entity):
        if entity.get_cardinal_direction_facing() == "south" or entity.get_cardinal_direction_facing() == "north":
            self.DIRECTION.setDirection("z")
        elif entity.get_cardinal_direction_facing() == "west" or entity.get_cardinal_direction_facing() == "east":
            self.DIRECTION.setDirection("x")
        super().finallyPlace(entity)
    @override
    def getProperty(self):
        return self.DIRECTION.getDirection()
    @override
    def getDefaultProperty(self):
        return "x"
    @override
    def getProperties(self):
        return self.DIRECTION.getDirectionKeys()