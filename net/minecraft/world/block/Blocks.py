from net.minecraft.world.block import Block, CardinalableBlock, OakSapling, GlassPaneBlock, StairBlock, LogBlock, \
    DoorBlock, SlabBlock, FenceBlock, TntBlock, FallingBlock

import net.minecraft.modloader.bus.EventBusRegistry as EventBusRegistry

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
    "oak_leaves":Block,
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
    "gravel":FallingBlock
}

modregistries={}

for (ns,n),c in EventBusRegistry.eventBus.getBlocks().items():
    registries[n]=c
    modregistries[n]=ns
