registries={}

def register(registry_type, resource_location, class_):
	if not registry_type in registries.keys():
		registries[registry_type]=[]
	registries[registry_type].append([resource_location, class_])
