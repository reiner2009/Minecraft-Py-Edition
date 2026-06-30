from net.minecraft.world.entity.FallingGravel import FallingGravel
from net.minecraft.world.entity.PlayerEntity import PlayerEntity
from net.minecraft.world.entity.PigEntity import PigEntity
from net.minecraft.world.entity.IgnitedTnt import IgnitedTnt
from net.minecraft.world.entity.FallingSand import FallingSand
import net.minecraft.modloader.bus.EventBusRegistry as EventBusRegistry

entities={
    "player":PlayerEntity,
    "pig":PigEntity,
    "ignited_tnt": IgnitedTnt,
    "falling_sand":FallingSand,
    "falling_gravel":FallingGravel
}

for (namespace, name), class_ in EventBusRegistry.eventBus.getEntities().items():
    entities[name]=class_
