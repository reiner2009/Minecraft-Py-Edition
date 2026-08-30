from net.minecraft.world.block.Block import Block
from net.minecraft.world.block.CardinalableBlock import CardinalableBlock
from net.minecraft.world.block.OakSapling import OakSapling
from net.minecraft.world.block.GlassPaneBlock import GlassPaneBlock
from net.minecraft.world.block.StairBlock import StairBlock
from net.minecraft.world.block.LogBlock import LogBlock
from net.minecraft.world.block.DoorBlock import DoorBlock
from net.minecraft.world.block.SlabBlock import SlabBlock
from net.minecraft.world.block.FenceBlock import FenceBlock
from net.minecraft.world.block.TntBlock import TntBlock
from net.minecraft.world.block.FallingBlock import FallingBlock
from net.minecraft.world.block.TrapdoorBlock import TrapdoorBlock
from net.minecraft.world.block.PostBlock import PostBlock
from net.minecraft.world.block.LeavesBlock import LeavesBlock

import net.minecraft.modloader.bus.EventBus as EventBus

registries={
    "bedrock":Block,
    "cobblestone":Block,
    "deepslate":LogBlock,
    "dirt":Block,
    "grass_block":Block,
    "oak_log":LogBlock,
    "oak_planks":Block,
    "stone":Block,
    "stone_bricks":Block,
    "white_wool":Block,
    "light_blue_wool":Block,
    "green_wool":Block,
    "black_wool":Block,
    "blue_wool":Block,
    "brown_wool":Block,
    "cyan_wool":Block,
    "gray_wool":Block,
    "light_gray_wool":Block,
    "lime_wool":Block,
    "magenta_wool":Block,
    "orange_wool":Block,
    "pink_wool":Block,
    "purple_wool":Block,
    "red_wool":Block,
    "yellow_wool":Block,
    "oak_leaves":LeavesBlock,
    "glass_block":Block,
    "smooth_stone":Block,
    "gold_block":Block,
    "diamond_block":Block,
    "lapis_block":Block,
    "iron_block":Block,
    "bricks":Block,
    "deepslate_bricks":Block,
    "polished_deepslate":Block,
    "copper_block":Block,
    "furnace":CardinalableBlock,
    "crafting_table":CardinalableBlock,
    "oak_sapling":OakSapling,
    "glass_pane":GlassPaneBlock,
    "oak_stair":StairBlock,
    "oak_door":DoorBlock,
    "oak_slab":SlabBlock,
    "oak_wood":Block,
    "oak_fence":FenceBlock,
    "tnt":TntBlock,
    "sand":FallingBlock,
    "gravel":FallingBlock,
    "oak_trapdoor":TrapdoorBlock,
    "white_stained_glass_block":Block,
    "orange_stained_glass_block":Block,
    "magenta_stained_glass_block":Block,
    "light_blue_stained_glass_block":Block,
    "yellow_stained_glass_block":Block,
    "lime_stained_glass_block":Block,
    "pink_stained_glass_block":Block,
    "gray_stained_glass_block":Block,
    "light_gray_stained_glass_block":Block,
    "cyan_stained_glass_block":Block,
    "purple_stained_glass_block":Block,
    "blue_stained_glass_block":Block,
    "brown_stained_glass_block":Block,
    "green_stained_glass_block":Block,
    "red_stained_glass_block":Block,
    "black_stained_glass_block":Block,
    "oak_post":PostBlock
}

modregistries={}

for (ns,n),c in EventBus.registryEventBus.getBlocks().items():
    registries[n]=c
    modregistries[n]=ns
