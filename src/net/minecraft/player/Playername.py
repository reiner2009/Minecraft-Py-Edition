import os
import net.minecraft.resources.DataLocation as DataLocation


base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
log_path = os.path.join(base_path, ".cache")
full_path = os.path.join(log_path, "launcher.txt")
try:
    with open(full_path, "r") as file:
        for line in file:
            playername = line.strip()
except FileNotFoundError:
        playername = "StevePy"
