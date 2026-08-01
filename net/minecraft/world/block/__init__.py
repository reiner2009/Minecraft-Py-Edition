from net.minecraft.client.Sounds import*
from net.minecraft.world.block.props import AxisProperty, FacingProperty, TwoDirectionsProperty, StairSetProperty, \
    DoorSetProperty, SlabSetProperty, TrapdoorSetProperty, FenceState
import net.minecraft.world.Features as features
import net.minecraft.resources.DataLocation as DataLocation
import net.minecraft.util.math.Raycast as Raycast
from net.minecraft.world.phys import AABB
from net.minecraft.util import Override
import random
import pickle
import gzip
import json

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
