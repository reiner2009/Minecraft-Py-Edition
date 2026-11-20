import net.mcpy.registry.Registry as Registry
import net.mcpy.registry.Registries as Registries
from net.mcpy.world.generator.Tree import Tree
from net.mcpy.resources.Identifier import Identifier

def registerFeature(id, class_):
	Registry.register(Registries.FEATURE, id, class_)
	return class_

TREE=registerFeature(Identifier(path="tree"), Tree)

def trigger():
	pass