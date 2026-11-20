registries={}

def register(registry_type, id, class_):
	if not registry_type in registries.keys():
		registries[registry_type]=[]
	registries[registry_type].append([id, class_])
