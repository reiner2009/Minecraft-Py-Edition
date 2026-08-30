import traceback

from net.minecraft.client.Textures import *
import net.minecraft.client.render.world.block.Models as Models
import json
import net.minecraft.resources.DataLocation as DataLocation
from net.minecraft.world.block.Blocks import registries
from net.minecraft.world.block.Block import Block

sound_categories=json.load(open(DataLocation.get_resource_path("assets/minecraft/sounds/sounds.json")))

block_place_sounds=sound_categories["categories"]["block_place"]

block_break_sounds=sound_categories["categories"]["block_break"]

blocks=registries.keys()

block_atlas=load_texture("assets/minecraft/textures/block/atlas.png")

block_atlas_data=json.load(open(DataLocation.get_resource_path("assets/minecraft/atlas_data/blocks.json")))
UV_MAP = block_atlas_data["values"]

render_data=json.load(open(DataLocation.get_resource_path("assets/minecraft/render/render_data.json")))

translucent_blocks=render_data["translucent"]
not_full_blocks=render_data["not_full"]
cutout_blocks=render_data["cutout"]

def cube_vertices(x, y, z, scale):
    return [
        (-1*scale+x,-1*scale+y,-1*scale+z), (1*scale+x,-1*scale+y,-1*scale+z), (1*scale+x,-1*scale+y,1*scale+z), (-1*scale+x,-1*scale+y,1*scale+z),
        (-1*scale+x,1*scale+y,-1*scale+z),  (1*scale+x,1*scale+y,-1*scale+z),  (1*scale+x,1*scale+y,1*scale+z),  (-1*scale+x,1*scale+y,1*scale+z)
    ]

def custom_cube_vertices(x, y, z, x0,y0,z0,x1,y1,z1, scale):
    return [
        (x0*scale+x,y0*scale+y,z0*scale+z), (x1*scale+x,y0*scale+y,z0*scale+z), (x1*scale+x,y0*scale+y,z1*scale+z), (x0*scale+x,y0*scale+y,z1*scale+z),
        (x0*scale+x,y1*scale+y,z0*scale+z), (x1*scale+x,y1*scale+y,z0*scale+z), (x1*scale+x,y1*scale+y,z1*scale+z), (x0*scale+x,y1*scale+y,z1*scale+z)
    ]

chunk = {}

def draw_block(vertices, surfaces, UVs, x, y, z, property="", not_cullable_surfaces=[False, False, False, False, False, False], preview=False):
    neighbors = [(0,-1,0), (0,1,0), (0,0,-1), (1,0,0), (0,0,1), (-1,0,0)]
    if preview == False:
        for i in range(6):
            dx, dy, dz = neighbors[i]
            neighbor=get_block(x+dx,y+dy,z+dz)
            neighborbool=(neighbor=="air")
            if neighborbool or (((neighbor in translucent_blocks and get_block(x,y,z)!=neighbor) or neighbor in cutout_blocks or neighbor in not_full_blocks) and not_cullable_surfaces[i]!="only_when_fully_covered") or not_cullable_surfaces[i]==True:
                glBegin(GL_QUADS)
                for j in range(4):
                    tx,ty=UVs[i][j]
                    vx, vy, vz = vertices[surfaces[i][j]]
                    glTexCoord2f(tx, ty)
                    glVertex3f(vx, vy, vz)
                glEnd()
            neigbor_data=get_block_data(x+dx,y+dy,z+dz)
            if (neighborbool or not_cullable_surfaces[i]=="only_when_fully_covered") and (neighbor=="glass_pane" and property=="x" and neigbor_data.getProperty()=="z") or (neighbor=="glass_pane" and property=="z" and neigbor_data.getProperty()=="x") or neighbor in not_full_blocks:
                glBegin(GL_QUADS)
                for j in range(4):
                    tx, ty = UVs[i][j]
                    vx, vy, vz = vertices[surfaces[i][j]]
                    glTexCoord2f(tx, ty)
                    glVertex3f(vx, vy, vz)
                glEnd()
    else:
        for i in range(6):
            glBegin(GL_QUADS)
            for j in range(4):
                tx, ty = UVs[i][j]
                vx, vy, vz = vertices[surfaces[i][j]]
                glTexCoord2f(tx, ty)
                glVertex3f(vx, vy, vz)
            glEnd()



def place_block(name, x, y, z, property="", preview=False, scale=1.0):
    global chunk
    data= Models.get_model(name, property)
    if data["type"]=="full_cube":
        texture_names = data["textures"]
        w, h = block_atlas_data["width"], block_atlas_data["height"]
        UVs = []
        for tex_name in texture_names:
            uv=UV_MAP[tex_name]
            UVs.append([((uv[0] + 1) / w, (uv[1]) / h), ((uv[0]) / w, (uv[1]) / h),((uv[0]) / w, (uv[1] + 1) / h), ((uv[0] + 1) / w, (uv[1] + 1) / h)])
        draw_block(
            cube_vertices(x*2, y*2, z*2, scale),
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
            preview=preview
        )
    if data["type"]=="custom_model":
        for element in data["elements"].values():
            custom_uv = element["custom_uv"]
            texture_names = element["textures"]
            UVs = []
            w, h = block_atlas_data["width"], block_atlas_data["height"]
            for i in range(6):
                uv=custom_uv[i]
                UVs_=[]
                if uv!=False:
                    for uv_ in uv:
                        UVs_.append([uv_[0]/w,uv_[1]/h])
                    UVs.append(UVs_)
                else:
                    uv=UV_MAP[texture_names[i]]
                    UVs.append([((uv[0] + 1) / w, (uv[1]) / h), ((uv[0]) / w, (uv[1]) / h), ((uv[0]) / w, (uv[1] + 1) / h),((uv[0] + 1) / w, (uv[1] + 1) / h)])
            vertices=element["vertices"]
            not_cullable_surfaces=element["not_cullable"]
            draw_block(
                custom_cube_vertices(x*2, y*2, z*2, *vertices, scale),
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
                property,
                not_cullable_surfaces,
                preview=preview
            )



def get_block(x_,y_,z_):
    x,y,z=round(x_),round(y_),round(z_)
    global chunk
    try:
        return chunk[(x,y,z)].getName()
    except:
        return "air"

def get_block_data(x_,y_,z_):
    x,y,z=round(x_),round(y_),round(z_)
    global chunk
    try:
        return chunk[(x,y,z)]
    except:
        return Block("air")

lines=[
    (0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)
]

def draw_block_preview(name, x, y, z, hit=False, property=""):
    if hit:
        glColor3f(1,0,0)
        glLineWidth(12)
    else:
        glColor3f(1,1,1)
        glLineWidth(12)
    if hit:
        glDisable(GL_TEXTURE_2D)
        glBegin(GL_LINES)
        for line in lines:
            for vertex in line:
                glVertex3fv(get_block_data(x,y,z).getVoxelShape(x,y,z)[vertex])
        glEnd()
    if not hit:
        glBindTexture(GL_TEXTURE_2D, block_atlas)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_BLEND)
        glEnable(GL_CULL_FACE)
        glDepthMask(GL_FALSE)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(1,1,1,0.5001)
        place_block(name,x,y,z, property)
        glDisable(GL_BLEND)
        glDepthMask(GL_TRUE)
