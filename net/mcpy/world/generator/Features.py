import net.mcpy.registry.Registry as Registry;
import net.mcpy.registry.Registries as Registries;
from net.mcpy.world.generator.Tree import Tree
from net.mcpy.resources.ResourceLocation import ResourceLocation

def registerFeature(resource_location, class_):
	Registry.register(Registries.FEATURE, resource_location, class_)
	return class_

TREE=registerFeature(ResourceLocation(path="tree"), Tree)
