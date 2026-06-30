from net.minecraft.world.block import Block
import net.minecraft.util.Logger as logger
from net.minecraft.chat.Chat import show_text

canTeleportPlayer=True

class CustomBlock(Block):
	def __init__(self, NAME):
		super().__init__(NAME)
	def onPlace(self, entity, block_sound_volume):
		super().onPlace(entity, block_sound_volume)
		if canTeleportPlayer:
			entity.spawn(*self.MAP_POSITION, *entity.get_entity_facing())
	def checkEntityInside(self, entity):
		x,y,z=entity.get_entity_position()
		pos=round(x),round(y),round(z)
		if pos == self.MAP_POSITION:
			return True
		else:
			return False
	def PlaceableBlockDuringInteraction(self, entity):
		return self.checkEntityInside(entity)
	def onInteraction(self, entity, block_sound_volume):
		global canTeleportPlayer
		if self.checkEntityInside(entity)==False:
			if entity.getMainhandItem()=="example_item":
				canTeleportPlayer=not canTeleportPlayer
				show_text("'canTeleportToPlayer' set to "+str(canTeleportPlayer), [255,255,255,2555])
		else:
			super().onInteraction(entity, block_sound_volume)
