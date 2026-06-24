from net.minecraft.sounds.Sounds import play_block_sound
from net.minecraft.world.block.props import AxisProperty, FacingProperty, TwoDirectionsProperty, StairSetProperty, \
    DoorSetProperty, SlabSetProperty
import net.minecraft.world.Features as features
import net.minecraft.resources.DataLocation as DataLocation
import net.minecraft.util.math.Raycast as Raycast
import random
import pickle
import gzip
import json

from net.minecraft.world.phys.VoxelShape import getVoxelShapeVertices

block_items=json.load(open(DataLocation.get_resource_path("data/minecraft/item/BlockItems.json")))

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
    def onPlace(self, entity, block_sound_volume):
        self.finallyPlace(entity, block_sound_volume)
    def onBreak(self, entity):
        pass
    def finallyPlace(self, entity, block_sound_volume):
        from net.minecraft.client.render.world.block.BlockRenderer import block_place_sounds
        from net.minecraft.sounds.Sounds import play_place_sound
        if self.NAME in block_place_sounds.keys():
            play_place_sound(block_place_sounds[self.NAME], block_sound_volume)
        else:
            play_place_sound("stone", block_sound_volume)
        reloadChunks()
    def setNewBlock(self, entity, X,Y,Z, reload=True):
        from net.minecraft.world.chunk.Chunk import get_block_data, get_block, set_block
        set_block(X, Y, Z, entity.getMainhandItem())
        get_block_data(X, Y, Z).setPropertyByPlayer(entity)
        entity.swing("right")
    def onInteraction(self, entity, block_sound_volume):
        from net.minecraft.world.block.Blocks import registries
        if entity.getMainhandItem() in registries:
            X, Y, Z, *_ = Raycast.get_pos(entity)
            if Raycast.get_neighbour_block(X, Y, Z):
                from net.minecraft.client.render.world.block.BlockRenderer import get_block_data
                self.setNewBlock(entity, X,Y,Z)
                get_block_data(X, Y, Z).onPlace(entity, block_sound_volume)
    def PlaceableBlockDuringInteraction(self, entity):
        return True

class LogBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.AXIS=AxisProperty("y")
    def setPropertyByPlayer(self, entity):
        if -45<entity.get_entity_facing()[1]<0 or 0<entity.get_entity_facing()[1]<45:
            if entity.get_cardinal_direction_facing()=="south" or entity.get_cardinal_direction_facing()=="north":
                self.AXIS.setAxis("z")
            elif entity.get_cardinal_direction_facing()=="west" or entity.get_cardinal_direction_facing()=="east":
                self.AXIS.setAxis("x")
        else:
            self.AXIS.setAxis("y")
    def getProperty(self,entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.AXIS.getAxis()
    def getDefaultProperty(self):
        return "y"
    def getProperties(self):
        return self.AXIS.getAxisKeys()

class CardinalableBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.FACING=FacingProperty()
    def setPropertyByPlayer(self, entity):
        self.FACING.setFacing(entity.get_cardinal_direction_facing())
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.FACING.getFacing()
    def getDefaultProperty(self):
        return "south"
    def getProperties(self):
        return self.FACING.getFacingKeys()

class OakSapling(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
    def finallyPlace(self, entity, block_sound_volume):
        spawnTree(*self.MAP_POSITION)
        super().finallyPlace(entity, block_sound_volume)

class GlassPaneBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.DIRECTION=TwoDirectionsProperty("x")
    def setPropertyByPlayer(self, entity):
        if entity.get_cardinal_direction_facing() == "south" or entity.get_cardinal_direction_facing() == "north":
            self.DIRECTION.setDirection("z")
        elif entity.get_cardinal_direction_facing() == "west" or entity.get_cardinal_direction_facing() == "east":
            self.DIRECTION.setDirection("x")
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.DIRECTION.getDirection()
    def getDefaultProperty(self):
        return "x"
    def getProperties(self):
        return self.DIRECTION.getDirectionKeys()
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
    def setPropertyByPlayer(self, entity):
        if -90 < entity.get_entity_facing()[1] < 0:
            self.VERTICAL_DIRECTION="1"
        if 0 < entity.get_entity_facing()[1] < 90:
            self.VERTICAL_DIRECTION="0"
        self.STAIR_SET.setStairSet(entity.get_cardinal_direction_facing()+self.VERTICAL_DIRECTION)
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.STAIR_SET.getStairSet()
    def getDefaultProperty(self):
        return "south0"
    def getProperties(self):
        return self.STAIR_SET.getStairSetKeys()

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
    def setProperty(self, property):
        self.DIRECTION.setDirection(property)
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.DIRECTION.getDirection()
    def setPropertyByPlayer(self, entity):
        from net.minecraft.world.chunk.Chunk import get_block
        if get_block(self.MAP_POSITION[0],self.MAP_POSITION[1]-1,self.MAP_POSITION[2])=="oak_door":
            self.VERTICAL_DIRECTION="0"
        self.DIRECTION.setDirection(entity.get_cardinal_direction_facing()+self.VERTICAL_DIRECTION)
    def getDefaultProperty(self):
        return "south0"
    def getProperties(self):
        return self.DIRECTION.getDirectionKeys()
    def setVerticalDirection(self, direction):
        self.VERTICAL_DIRECTION=direction
    def getVerticalDirection(self):
        return self.VERTICAL_DIRECTION
    def setState(self, state):
        self.STATE=state
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
    def onBreak(self, entity):
        self.up_nighbour = self.MAP_POSITION[0], self.MAP_POSITION[1] + 1, self.MAP_POSITION[2]
        self.down_nighbour = self.MAP_POSITION[0], self.MAP_POSITION[1] - 1, self.MAP_POSITION[2]
        from net.minecraft.world.chunk.Chunk import set_block, get_block_data, get_block
        if get_block(*self.up_nighbour)=="oak_door":
            if get_block_data(*self.up_nighbour).getVerticalDirection()=="1":
                set_block(*self.up_nighbour, "air")
        if get_block(*self.down_nighbour) == "oak_door":
            if get_block_data(*self.down_nighbour).getVerticalDirection()=="0":
                set_block(*self.down_nighbour, "air")
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
    def PlaceableBlockDuringInteraction(self, entity):
        return False

class SlabBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
        self.VERICAL_POS=SlabSetProperty()
    def getProperties(self):
        return self.VERICAL_POS.getVerticalPosKeys()
    def getProperty(self, entity=None):
        if entity:
            self.setPropertyByPlayer(entity)
        return self.VERICAL_POS.getVerticalPos()
    def setPropertyByPlayer(self, entity):
        if -90 < entity.get_entity_facing()[1] < 0:
            self.VERICAL_POS.setVerticalPos("up")
        if 0 < entity.get_entity_facing()[1] < 90:
            self.VERICAL_POS.setVerticalPos("down")
    def getDefaultProperty(self):
        return "down"
    def getVoxelShape(self, x, y, z):
        self.VOXEL_SHAPE_MAP = {
            "up": [(-1, 0, -1), (1, 0, -1), (1, 0, 1), (-1, 0, 1), (-1, 1, -1), (1, 1, -1), (1, 1, 1),(-1, 1, 1)],
            "down":[(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (-1, 0, -1), (1, 0, -1), (1, 0, 1),(-1, 0, 1)]
        }
        self.VOXEL_SHAPE = self.VOXEL_SHAPE_MAP[self.VERICAL_POS.getVerticalPos()]
        return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)

class FenceBlock(GlassPaneBlock):
    def __init__(self, NAME):
        super().__init__(NAME)
    def getVoxelShape(self, x, y, z):
        if self.DIRECTION.getDirection() == "x":
            self.VOXEL_SHAPE = [(-0.25, -1, -1), (0.25, -1, -1), (0.25, -1, 1), (-0.25, -1, 1), (-0.25, 1, -1),(0.25, 1, -1), (0.25, 1, 1), (-0.25, 1, 1)]
        if self.DIRECTION.getDirection() == "z":
            self.VOXEL_SHAPE = [(-1, -1, -0.25), (1, -1, -0.25), (1, -1, 0.25), (-1, -1, 0.25), (-1, 1, -0.25),(1, 1, -0.25), (1, 1, 0.25), (-1, 1, 0.25)]
        return getVoxelShapeVertices(x, y, z, self.VOXEL_SHAPE)

class TntBlock(Block):
    def __init__(self, NAME):
        super().__init__(NAME)
    def onInteraction(self, entity, block_sound_volume):
        if entity.getMainhandItem()=="flint_and_steel":
            from net.minecraft.entity.Entities import entites
            from net.minecraft.world.chunk.Chunk import set_block
            self.primed_tnt=entites["primed_tnt"]()
            self.primed_tnt.set_sound_volume(block_sound_volume)
            self.primed_tnt.spawn(*self.MAP_POSITION)
            set_block(*self.MAP_POSITION, "air")
            reloadChunks()
            play_block_sound("fuse", block_sound_volume)
        else:
            super().onInteraction(entity, block_sound_volume)
