import gzip
import pickle
import os
from net.minecraft.resources.DataLocation import get_save_system
from net.minecraft.world.block.Blocks import registries

chunk={}

base_path = os.path.join(os.environ[get_save_system()], ".minecraft-py")
world = os.path.join(base_path, "world")
full_path = os.path.join(world, "chunks.dat")
with open(full_path, "rb") as f:
    chunk=pickle.load(f)

for k, v in chunk.items():
    chunk[k]=registries[v](v)

with gzip.open(full_path, "wb", compresslevel=9) as f:
    pickle.dump(chunk, f)