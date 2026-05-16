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

render_data=json.load(open(DataLocation.get_resource_path("assets/minecraft/render/render_data.json")))

translucent_blocks=render_data["translucent"]

cutout_blocks=render_data["cutout"]

def cube_vertices(x, y, z):
    return [
        (-1+x,-1+y,-1+z), (1+x,-1+y,-1+z), (1+x,-1+y,1+z), (-1+x,-1+y,1+z),
        (-1+x,1+y,-1+z),  (1+x,1+y,-1+z),  (1+x,1+y,1+z),  (-1+x,1+y,1+z)
    ]

def custom_cube_vertices(x, y, z, x0,y0,z0,x1,y1,z1):
    return [
        (x0+x,y0+y,z0+z), (x1+x,y0+y,z0+z), (x1+x,y0+y,z1+z), (x0+x,y0+y,z1+z),
        (x0+x,y1+y,z0+z), (x1+x,y1+y,z0+z), (x1+x,y1+y,z1+z), (x0+x,y1+y,z1+z)
    ]

chunk = {}

def draw_block(vertices, surfaces, UVs, x, y, z, not_cullable_surfaces=[False, False, False, False, False, False]):
    neighbors = [(0,-1,0), (0,1,0), (0,0,-1), (1,0,0), (0,0,1), (-1,0,0)]
    glEnable(GL_TEXTURE_2D)
    for i in range(6):
        dx, dy, dz = neighbors[i]
        neighbor=get_block(x+dx,y+dy,z+dz)
        uv = UVs[i] if i < len(UVs) else UVs[0]
        if (neighbor=="air" or (neighbor in translucent_blocks and get_block(x,y,z)!=neighbor) or neighbor in cutout_blocks) or not_cullable_surfaces[i]:
            w,h=block_atlas_data["width"], block_atlas_data["height"]
            uv_map = [((uv[0] + 1) / w, (uv[1]) / h), ((uv[0]) / w, (uv[1]) / h),
                      ((uv[0]) / w, (uv[1] + 1) / h), ((uv[0] + 1) / w, (uv[1] + 1) / h)]
            glBegin(GL_QUADS)
            for j in range(4):
                tx,ty=uv_map[j]
                vx, vy, vz = vertices[surfaces[i][j]]
                glTexCoord2f(tx,ty)
                glVertex3f(vx, vy, vz)
            glEnd()

def place_block(name, x, y, z, property=""):
    global chunk
    data= Models.get_model(name, property)
    if data["type"]=="full_cube":
        texture_names = data["textures"]
        UVs = []
        for tex_name in texture_names:
            UVs.append(UV_MAP[tex_name])
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
    if data["type"]=="custom_model":
        for element in data["elements"].values():
            texture_names = element["textures"]
            UVs = []
            for tex_name in texture_names:
                UVs.append(UV_MAP[tex_name])
            vertices=element["vertices"]
            not_cullable_surfaces=element["not_cullable"]
            draw_block(
                custom_cube_vertices(x*2, y*2, z*2, *vertices),
                [
                    (0, 1, 2, 3),
                    (7, 6, 5, 4),
                    (4, 5, 1, 0),
                    (5, 6, 2, 1),
                    (6, 7, 3, 2),
                    (7, 4, 0, 3)
                ],
                UVs,
                x,y,z,
                not_cullable_surfaces
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