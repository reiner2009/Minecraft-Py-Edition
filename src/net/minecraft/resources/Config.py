from jproperties import Properties
import os
import net.minecraft.resources.DataLocation as DataLocation

base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
log_path = os.path.join(base_path, ".config")
os.makedirs(log_path, exist_ok=True)
full_path = os.path.join(log_path, "client.properties")

if not os.path.exists(full_path):
    with open(full_path, "wb") as f:
        pass

p = Properties()

def load_config(key):
    global p
    with open(full_path, "rb") as f:
        p.load(f, "utf-8")
    return p[key].data

def save_config(key, value):
    global p
    p[key] = str(value)
    with open(full_path, "wb") as f:
        p.store(f, encoding="utf-8")