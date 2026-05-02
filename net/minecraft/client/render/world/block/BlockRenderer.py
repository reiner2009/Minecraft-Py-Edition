from net.minecraft.textures.Textures import *
import net.minecraft.sounds.Sounds as sounds
import net.minecraft.client.render.world.block.Models as Models

sound_categorys_dig={
    "stone_bricks":sounds.dig_stone_music_tracks,
    "cobblestone":sounds.dig_stone_music_tracks,
    "stone":sounds.dig_stone_music_tracks,
    "deepslate":sounds.dig_stone_music_tracks,
    "bedrock":sounds.dig_stone_music_tracks,
    "dirt":sounds.dig_gravel_music_tracks,
    "grass_block":sounds.dig_grass_music_tracks,
    "oak_planks":sounds.dig_wood_music_tracks,
    "oak_log":sounds.dig_wood_music_tracks,
    "white_wool":sounds.dig_cloth_music_tracks,
    "light_blue_wool":sounds.dig_cloth_music_tracks,
    "green_wool":sounds.dig_cloth_music_tracks,
    "black_wool":sounds.dig_cloth_music_tracks,
    "blue_wool":sounds.dig_cloth_music_tracks,
    "brown_wool":sounds.dig_cloth_music_tracks,
    "cyan_wool":sounds.dig_cloth_music_tracks,
    "gray_wool":sounds.dig_cloth_music_tracks,
    "light_gray_wool":sounds.dig_cloth_music_tracks,
    "lime_wool":sounds.dig_cloth_music_tracks,
    "magenta_wool":sounds.dig_cloth_music_tracks,
    "orange_wool":sounds.dig_cloth_music_tracks,
    "pink_wool":sounds.dig_cloth_music_tracks,
    "purple_wool":sounds.dig_cloth_music_tracks,
    "red_wool":sounds.dig_cloth_music_tracks,
    "yellow_wool":sounds.dig_cloth_music_tracks,
    "oak_leaves":sounds.dig_grass_music_tracks,
    "glass_block":sounds.dig_stone_music_tracks,
    "glass_block_break":sounds.glass_music_tracks,
    "gold_block":sounds.dig_stone_music_tracks,
    "smooth_stone":sounds.dig_stone_music_tracks,
    "diamond_block":sounds.dig_stone_music_tracks,
    "lapis_block":sounds.dig_stone_music_tracks,
    "iron_block":sounds.dig_stone_music_tracks,
    "bricks":sounds.dig_stone_music_tracks,
    "deepslate_bricks":sounds.dig_stone_music_tracks,
    "polished_deepslate":sounds.dig_stone_music_tracks
}

blocks= Models.model_names

block_atlas=load_texture("assets/minecraft/textures/block/atlas.png")

UV_MAP = {
    "stone_bricks": [4,5],
    "dirt": [5,1],
    "grass_block_side": [2,2],
    "grass_block_top": [3,2],
    "stone": [5,5],
    "bedrock": [0,0],
    "deepslate": [3,1],
    "deepslate_top": [2,1],
    "cobblestone":[5,0],
    "oak_planks":[3,4],
    "oak_log":[2,4],
    "oak_log_top":[1,4],
    "error":[2,6],
    "white_wool":[0,6],
    "light_blue_wool":[2,3],
    "green_wool":[5,2],
    "black_wool":[1,0],
    "blue_wool":[2,0],
    "brown_wool":[4,0],
    "cyan_wool":[0,1],
    "gray_wool":[4,2],
    "light_gray_wool":[3,3],
    "lime_wool":[4,3],
    "magenta_wool":[5,3],
    "orange_wool":[4,4],
    "pink_wool":[5,4],
    "purple_wool":[1,5],
    "red_wool":[2,5],
    "yellow_wool":[1,6],
    "oak_leaves":[0,4],
    "glass_block":[0,2],
    "smooth_stone":[3,5],
    "gold_block":[1,2],
    "diamond_block":[4,1],
    "lapis_block":[1,3],
    "iron_block":[0,3],
    "bricks":[3,0],
    "deepslate_bricks":[1,1],
    "polished_deepslate":[0,5]
}

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
            uv_map = [((uv[0]) / 6, (uv[1]) / 7), ((uv[0] + 1) / 6, (uv[1]) / 7),
                      ((uv[0] + 1) / 6, (uv[1] + 1) / 7), ((uv[0]) / 6, (uv[1] + 1) / 7)]
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