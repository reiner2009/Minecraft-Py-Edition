from typing import override

from net.minecraft.world.block.props import AxisProperty, FacingProperty, TwoDirectionsProperty, StairSetProperty, \
    DoorSetProperty, DoorStateProperty
import net.minecraft.world.Features as features
import net.minecraft.resources.DataLocation as DataLocation
import net.minecraft.util.math.Raycast as Raycast
import random
import pickle
import gzip

from net.minecraft.world.phys.VoxelShape import getVoxelShapeVertices


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
        self.NAME = NAME
        self.MAP_POSITION = (0,0,0)
    def setPos(self, x, y,z):
        self.MAP_POSITION = (x,y,z)
    def getName(self):
        return self.NAME
    def setPropertyByPlayer(self, entity):
        pass
    def getProperty(self, entity=None):
        return ""
    def getDefaultProperty(self):
        return ""
    def getProperties(self):
        return [""]
    def getVoxelShape(self, x, y, z):
        self.VOXEL_SHAPE = [(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (-1, 1, -1), (1, 1, -1), (1, 1, 1),(-1, 1, 1)]
        return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)
    def onPlace(self, entity):
        self.finallyPlace(entity)
    def onBreak(self, entity):
        pass
    def finallyPlace(self, entity):
        reloadChunks()
    def setNewBlock(self, entity, block_sound_volume, X,Y,Z, reload=True):
        from net.minecraft.client.render.world.block.BlockRenderer import block_place_sounds
        from net.minecraft.world.chunk.Chunk import get_block_data, get_block, set_block
        from net.minecraft.sounds.Sounds import play_place_sound
        set_block(X, Y, Z, entity.getMainhandItem())
        get_block_data(X, Y, Z).setPropertyByPlayer(entity)
        block = get_block(X, Y, Z)
        if block in block_place_sounds.keys():
            play_place_sound(block_place_sounds[block], block_sound_volume)
        else:
            play_place_sound("stone", block_sound_volume)
        entity.swing("right")
    def onInteraction(self, entity, block_sound_volume):
        X, Y, Z, *_ = Raycast.get_pos(entity)
        if Raycast.get_neighbour_block(X, Y, Z):
            from net.minecraft.client.render.world.block.BlockRenderer import get_block_data
            self.setNewBlock(entity, block_sound_volume, X,Y,Z)
            get_block_data(X, Y, Z).onPlace(entity)

class LogBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.AXIS=AxisProperty("y")
    @override
    def setPropertyByPlayer(self, entity):
        if -45<entity.get_entity_facing()[1]<0 or 0<entity.get_entity_facing()[1]<45:
            if entity.get_cardinal_direction_facing()=="south" or entity.get_cardinal_direction_facing()=="north":
                self.AXIS.setAxis("z")
            elif entity.get_cardinal_direction_facing()=="west" or entity.get_cardinal_direction_facing()=="east":
                self.AXIS.setAxis("x")
        else:
            self.AXIS.setAxis("y")
    @override
    def getProperty(self,entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
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
    def setPropertyByPlayer(self, entity):
        self.FACING.setFacing(entity.get_cardinal_direction_facing())
    @override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
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

class GlassPaneBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.DIRECTION=TwoDirectionsProperty("x")
    @override
    def setPropertyByPlayer(self, entity):
        if entity.get_cardinal_direction_facing() == "south" or entity.get_cardinal_direction_facing() == "north":
            self.DIRECTION.setDirection("z")
        elif entity.get_cardinal_direction_facing() == "west" or entity.get_cardinal_direction_facing() == "east":
            self.DIRECTION.setDirection("x")
    @override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.DIRECTION.getDirection()
    @override
    def getDefaultProperty(self):
        return "x"
    @override
    def getProperties(self):
        return self.DIRECTION.getDirectionKeys()
    @override
    def getVoxelShape(self, x, y, z):
        if self.DIRECTION.getDirection()=="x":
            self.VOXEL_SHAPE = [(-0.125, -1, -1), (0.125, -1, -1), (0.125, -1, 1), (-0.125, -1, 1), (-0.125, 1, -1), (0.125, 1, -1), (0.125, 1, 1),(-0.125, 1, 1)]
        if self.DIRECTION.getDirection()=="z":
            self.VOXEL_SHAPE = [(-1, -1, -0.125), (1, -1, -0.125), (1, -1, 0.125), (-1, -1, 0.125), (-1, 1, -0.125), (1, 1, -0.125), (1, 1, 0.125), (-1, 1, 0.125)]
        return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)

class StairBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.STAIR_SET=StairSetProperty("south0")
        self.VERTICAL_DIRECTION="0"
    @override
    def setPropertyByPlayer(self, entity):
        if -90 < entity.get_entity_facing()[1] < 0:
            self.VERTICAL_DIRECTION="1"
        if 0 < entity.get_entity_facing()[1] < 90:
            self.VERTICAL_DIRECTION="0"
        self.STAIR_SET.setStairSet(entity.get_cardinal_direction_facing()+self.VERTICAL_DIRECTION)
    @override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.STAIR_SET.getStairSet()
    @override
    def getDefaultProperty(self):
        return "south0"
    @override
    def getProperties(self):
        return self.STAIR_SET.getStairSetKeys()

class DoorBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.DIRECTION=DoorSetProperty()
        self.STATE=DoorStateProperty()
        self.VERTICAL_DIRECTION="0"
    def setProperty(self, property):
        self.DIRECTION.setDirection(property)
    @override
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.DIRECTION.getDirection()
    @override
    def setPropertyByPlayer(self, entity):
        from net.minecraft.world.chunk.Chunk import get_block
        if get_block(self.MAP_POSITION[0],self.MAP_POSITION[1]-1,self.MAP_POSITION[2])=="oak_door":
            self.VERTICAL_DIRECTION="1"
        self.DIRECTION.setDirection(entity.get_cardinal_direction_facing()+self.VERTICAL_DIRECTION)
    @override
    def getDefaultProperty(self):
        return "south0"
    @override
    def getProperties(self):
        return self.DIRECTION.getDirectionKeys()
    @override
    def onPlace(self, entity):
        from net.minecraft.world.chunk.Chunk import set_block, get_block, get_block_data
        if get_block(self.MAP_POSITION[0],self.MAP_POSITION[1]+1,self.MAP_POSITION[2])=="air":
            set_block(self.MAP_POSITION[0],self.MAP_POSITION[1]+1,self.MAP_POSITION[2], "oak_door")
            super().finallyPlace(entity)
        else:
            set_block(*self.MAP_POSITION, "air")
    @override
    def onBreak(self, entity):
        from net.minecraft.world.chunk.Chunk import set_block, get_block
        if get_block(self.MAP_POSITION[0],self.MAP_POSITION[1]+1,self.MAP_POSITION[2])=="oak_door":
            set_block(self.MAP_POSITION[0],self.MAP_POSITION[1]+1,self.MAP_POSITION[2], "air")
        if get_block(self.MAP_POSITION[0],self.MAP_POSITION[1]-1,self.MAP_POSITION[2])=="oak_door":
            set_block(self.MAP_POSITION[0],self.MAP_POSITION[1]-1,self.MAP_POSITION[2], "air")