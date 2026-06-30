import net.minecraft.modloader.bus.EventBusRegistry as EventBusRegistry

items=["flint_and_steel"]

for namespace, name in EventBusRegistry.eventBus.getItems().items():
    items.append(name)
