import net.minecraft.modloader.bus.EventBus as EventBus

items=["flint_and_steel"]

for namespace, name in EventBus.registryEventBus.getItems().items():
    items.append(name)
