from net.minecraft.textures.Textures import *
import net.minecraft.client.render.world.block.Models as Models
import json
import net.minecraft.resources.DataLocation as DataLocation

block_place_sounds={
    "stone_bricks":"stone",
    "cobblestone":"stone",
    "stone":"stone",
    "deepslate":"stone",
    "bedrock":"stone",
    "dirt":"gravel",
    "grass_block":"grass",
    "oak_planks":"wood",
    "oak_log":"wood",
    "white_wool":"cloth",
    "light_blue_wool":"cloth",
    "green_wool":"cloth",
    "black_wool":"cloth",
    "blue_wool":"cloth",
    "brown_wool":"cloth",
    "cyan_wool":"cloth",
    "gray_wool":"cloth",
    "light_gray_wool":"cloth",
    "lime_wool":"cloth",
    "magenta_wool":"cloth",
    "orange_wool":"cloth",
    "pink_wool":"cloth",
    "purple_wool":"cloth",
    "red_wool":"cloth",
    "yellow_wool":"cloth",
    "oak_leaves":"grass",
    "glass_block":"stone",
    "gold_block":"stone",
    "smooth_stone":"stone",
    "diamond_block":"stone",
    "lapis_block":"stone",
    "iron_block":"stone",
    "bricks":"stone",
    "deepslate_bricks":"stone",
    "polished_deepslate":"stone",
    "copper_block":"stone"
}

block_break_sounds={
    "glass_block":"glass"
}

blocks= Models.model_names

block_atlas=load_texture("assets/minecraft/textures/block/atlas.png")

block_atlas_data=json.load(open(DataLocation.get_resource_path("assets/minecraft/atlas_data/blocks.json")))
UV_MAP = block_atlas_data["values"]

translucent_blocks=[
    "glass_block"
]

cutout_blocks=[
    "oak_leaves"
]

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

def place_block(name, x, y, z):
    global chunk
    data= Models.get_model(name)
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
        return chunk[(x,y,z)]
    except:
        return "air"

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