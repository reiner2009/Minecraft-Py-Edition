from net.minecraft.textures.Textures import *
import net.minecraft.client.render.world.block.Models as Models
import json
import net.minecraft.resources.DataLocation as DataLocation
from net.minecraft.world.block.Blocks import registries

sound_categories=json.load(open(DataLocation.get_resource_path("assets/minecraft/sounds/sounds.json")))

block_place_sounds=sound_categories["categories"]["block_place"]

block_break_sounds=sound_categories["categories"]["block_break"]

blocks= registries.keys()

block_atlas=load_texture("assets/minecraft/textures/block/atlas.png")

block_atlas_data=json.load(open(DataLocation.get_resource_path("assets/minecraft/atlas_data/blocks.json")))
UV_MAP = block_atlas_data["values"]

render_data=json.load(open(DataLocation.get_resource_path("assets/minecraft/render_data.json")))

translucent_blocks=render_data["translucent"]

cutout_blocks=render_data["cutout"]

def cube_vertices(x, y, z):
    return [
        (-1+x,-1+y,-1+z), (1+x,-1+y,-1+z), (1+x,-1+y,1+z), (-1+x,-1+y,1+z),
        (-1+x,1+y,-1+z),  (1+x,1+y,-1+z),  (1+x,1+y,1+z),  (-1+x,1+y,1+z)
    ]

chunk = {}

def draw_block(vertices, surfaces, UVs, x, y, z):
    neighbors = [(0,-1,0), (0,1,0), (0,0,-1), (1,0,0), (0,0,1), (-1,0,0)]
    glEnable(GL_TEXTURE_2D)
    for i in range(6):
        dx, dy, dz = neighbors[i]
        neighbor=get_block(x+dx,y+dy,z+dz)
        uv = UVs[i] if i < len(UVs) else UVs[0]
        if (neighbor=="air" or (neighbor in translucent_blocks and get_block(x,y,z)!=neighbor) or neighbor in cutout_blocks):
            glBegin(GL_QUADS)
            w,h=block_atlas_data["width"], block_atlas_data["height"]
            uv_map = [((uv[0]) / w, (uv[1]) / h), ((uv[0] + 1) / w, (uv[1]) / h),
                      ((uv[0] + 1) / w, (uv[1] + 1) / h), ((uv[0]) / w, (uv[1] + 1) / h)]
            for j in range(4):
                tx,ty=uv_map[j]
                vx, vy, vz = vertices[surfaces[i][j]]
                glTexCoord2f(tx,ty)
                glVertex3f(vx, vy, vz)
            glEnd()

def place_block(name, x, y, z, property=""):
    global chunk
    data= Models.get_model(name, property)
    texture_names = data["textures"]
    UVs = []
    if isinstance(texture_names, dict):
        key_map = ["down","up","north","east","south","west"]
        for key in key_map:
            tex_name = texture_names.get(key)
            if tex_name in UV_MAP:
                UVs.append(UV_MAP[tex_name])
            else:
                UVs.append(UV_MAP[list(texture_names.values())[0]])
    elif isinstance(texture_names, list):
        for tex_name in texture_names:
            UVs.append(UV_MAP[tex_name])
        while len(UVs) < 6:
            UVs.append(UVs[0])
    else:
        UVs = [UV_MAP[texture_names]]*6
    draw_block(
        cube_vertices(x*2, y*2, z*2),
        [
            (0, 1, 2, 3),
            (7, 6, 5, 4),
            (4, 5, 1, 0),
            (5, 6, 2, 1),
            (6, 7, 3, 2),
            (7, 4, 0, 3)
        ],
        UVs,
        x,y,z
    )

def get_block(x,y,z):
    global chunk
    try:
        return chunk[(x,y,z)].getName()
    except:
        return "air"

def get_block_data(x,y,z):
    global chunk
    try:
        return chunk[(x,y,z)]
    except:
        return None

lines=[
    (0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)
]

def draw_block_preview(x, y, z, hit=False):
    glDisable(GL_TEXTURE_2D)
    if hit:
        glColor3f(1,0,0)
        glLineWidth(12)
    else:
        glColor3f(1,1,1)
        glLineWidth(12)
    glBegin(GL_LINES)
    if hit:
        for line in lines:
            for vertex in line:
                glVertex3fv(cube_vertices(x*2, y*2, z*2)[vertex])
    else:
        for line in lines:
            for vertex in line:
                glVertex3fv(cube_vertices(x*2, y*2, z*2)[vertex])
    glEnd()