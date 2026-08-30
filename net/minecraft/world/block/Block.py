from net.minecraft.world.block import*

class Block:
    def __init__(self, NAME):
        self.NAME = NAME
        self.MAP_POSITION = (0,0,0)
        self.COLLISION_SHAPE=AABB(-0.5, -0.5, -0.5, 0.5, 0.5, 0.5, *self.MAP_POSITION)
    def setPos(self, x, y,z):
        self.MAP_POSITION = (x,y,z)
        self.COLLISION_SHAPE=AABB(-0.5, -0.5, -0.5, 0.5, 0.5, 0.5, *self.MAP_POSITION)
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
    def getCollisionShape(self):
        return self.COLLISION_SHAPE
    def onPlace(self, entity, block_sound_volume):
        self.finallyPlace(entity, block_sound_volume)
    def onBreak(self, entity):
        pass
    def finallyPlace(self, entity, block_sound_volume):
        from net.minecraft.client.render.world.block.BlockRenderer import block_place_sounds
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
            if X and Y and Z:
                from net.minecraft.client.render.world.block.BlockRenderer import get_block_data
                self.temp_collisions_check=registries[entity.getMainhandItem()](entity.getMainhandItem())
                self.temp_collisions_check.setPos(X,Y,Z)
                self.temp_collisions_check.setPropertyByPlayer(entity)
                if (not entity.getHitbox().intersects(self.temp_collisions_check.getCollisionShape())) or (not self.temp_collisions_check.hasCollision()):
                    self.setNewBlock(entity, X,Y,Z)
                    get_block_data(X, Y, Z).onPlace(entity, block_sound_volume)
    def placeableBlockDuringInteraction(self, entity):
        return True
    def onExplode(self, v):
        from net.minecraft.world.chunk.Chunk import set_block
        set_block(*self.MAP_POSITION, "air")
    def update(self):
        pass
    def hasCollision(self):
        return self.NAME!="air"
