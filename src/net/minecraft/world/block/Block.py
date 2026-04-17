from net.minecraft.textures.Textures import *
import net.minecraft.world.block.Models as models
import net.minecraft.sounds.Sounds as sounds

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
    "deepslate_bricks":sounds.dig_stone_music_tracks
}

blocks=models.model_names

stone_bricks_texture = load_texture("assets/minecraft/textures/block/stone_bricks.png")
dirt_texture = load_texture("assets/minecraft/textures/block/dirt.png")
grass_block_side_texture = load_texture("assets/minecraft/textures/block/grass_block_side.png")
grass_block_top_texture = load_texture("assets/minecraft/textures/block/grass_block_top.png")
stone_texture = load_texture("assets/minecraft/textures/block/stone.png")
bedrock_texture = load_texture("assets/minecraft/textures/block/bedrock.png")
deepslate_texture = load_texture("assets/minecraft/textures/block/deepslate.png")
deepslate_top_texture = load_texture("assets/minecraft/textures/block/deepslate_top.png")
cobblestone_texture=load_texture("assets/minecraft/textures/block/cobblestone.png")
oak_planks_texture=load_texture("assets/minecraft/textures/block/oak_planks.png")
oak_log_texture=load_texture("assets/minecraft/textures/block/oak_log.png")
oak_log_top_texture=load_texture("assets/minecraft/textures/block/oak_log_top.png")
white_wool_texture=load_texture("assets/minecraft/textures/block/white_wool.png")
light_blue_wool_texture=load_texture("assets/minecraft/textures/block/light_blue_wool.png")
green_wool_texture=load_texture("assets/minecraft/textures/block/green_wool.png")
black_wool_texture=load_texture("assets/minecraft/textures/block/black_wool.png")
blue_wool_texture=load_texture("assets/minecraft/textures/block/blue_wool.png")
brown_wool_texture=load_texture("assets/minecraft/textures/block/brown_wool.png")
cyan_wool_texture=load_texture("assets/minecraft/textures/block/cyan_wool.png")
gray_wool_texture=load_texture("assets/minecraft/textures/block/gray_wool.png")
light_gray_wool_texture=load_texture("assets/minecraft/textures/block/light_gray_wool.png")
lime_wool_texture=load_texture("assets/minecraft/textures/block/lime_wool.png")
magenta_wool_texture=load_texture("assets/minecraft/textures/block/magenta_wool.png")
orange_wool_texture=load_texture("assets/minecraft/textures/block/orange_wool.png")
pink_wool_texture=load_texture("assets/minecraft/textures/block/pink_wool.png")
purple_wool_texture=load_texture("assets/minecraft/textures/block/purple_wool.png")
red_wool_texture=load_texture("assets/minecraft/textures/block/red_wool.png")
yellow_wool_texture=load_texture("assets/minecraft/textures/block/yellow_wool.png")
oak_leaves_texture=load_texture("assets/minecraft/textures/block/oak_leaves.png")
glass_block_texture=load_texture("assets/minecraft/textures/block/glass.png")
smooth_stone_texture=load_texture("assets/minecraft/textures/block/smooth_stone.png")
gold_block_texture=load_texture("assets/minecraft/textures/block/gold_block.png")
diamond_block_texture=load_texture("assets/minecraft/textures/block/diamond_block.png")
lapis_block_texture=load_texture("assets/minecraft/textures/block/lapis_block.png")
iron_block_texture=load_texture("assets/minecraft/textures/block/iron_block.png")
bricks_texture=load_texture("assets/minecraft/textures/block/bricks.png")
deepslate_bricks_texture=load_texture("assets/minecraft/textures/block/deepslate_bricks.png")
error_texture=load_texture("assets/minecraft/textures/error.png")

TEXTURE_MAP = {
    "stone_bricks": stone_bricks_texture,
    "dirt": dirt_texture,
    "grass_block_side": grass_block_side_texture,
    "grass_block_top": grass_block_top_texture,
    "stone": stone_texture,
    "bedrock": bedrock_texture,
    "deepslate": deepslate_texture,
    "deepslate_top": deepslate_top_texture,
    "cobblestone":cobblestone_texture,
    "oak_planks":oak_planks_texture,
    "oak_log":oak_log_texture,
    "oak_log_top":oak_log_top_texture,
    "error":error_texture,
    "white_wool":white_wool_texture,
    "light_blue_wool":light_blue_wool_texture,
    "green_wool":green_wool_texture,
    "black_wool":black_wool_texture,
    "blue_wool":blue_wool_texture,
    "brown_wool":brown_wool_texture,
    "cyan_wool":cyan_wool_texture,
    "gray_wool":gray_wool_texture,
    "light_gray_wool":light_gray_wool_texture,
    "lime_wool":lime_wool_texture,
    "magenta_wool":magenta_wool_texture,
    "orange_wool":orange_wool_texture,
    "pink_wool":pink_wool_texture,
    "purple_wool":purple_wool_texture,
    "red_wool":red_wool_texture,
    "yellow_wool":yellow_wool_texture,
    "oak_leaves":oak_leaves_texture,
    "glass_block":glass_block_texture,
    "gold_block":gold_block_texture,
    "smooth_stone":smooth_stone_texture,
    "diamond_block":diamond_block_texture,
    "lapis_block":lapis_block_texture,
    "iron_block":iron_block_texture,
    "bricks":bricks_texture,
    "deepslate_bricks":deepslate_bricks_texture
}

translucent_blocks=[
    "glass_block"
]

cutout_blocks=[
    "oak_leaves"
]

green_textures=[
    TEXTURE_MAP["grass_block_top"],
    TEXTURE_MAP["oak_leaves"]
]

def cube_vertices(x, y, z):
    return [
        (-1+x,-1+y,-1+z), (1+x,-1+y,-1+z), (1+x,-1+y,1+z), (-1+x,-1+y,1+z),
        (-1+x,1+y,-1+z),  (1+x,1+y,-1+z),  (1+x,1+y,1+z),  (-1+x,1+y,1+z)
    ]

chunk = {}

def draw_block(vertices, surfaces, tex_coords, textures, x, y, z, color=[1,1,1,1]):
    neighbors = [(0,-1,0), (0,1,0), (0,0,-1), (1,0,0), (0,0,1), (-1,0,0)]
    glEnable(GL_TEXTURE_2D)
    glColor4f(*color)
    for i in range(6):
        dx, dy, dz = neighbors[i]
        neighbor=get_block(x+dx,y+dy,z+dz)
        texture = textures[i] if i < len(textures) else textures[0]
        if (neighbor=="air" or (neighbor in translucent_blocks and get_block(x,y,z)!=neighbor) or neighbor in cutout_blocks):
            glBindTexture(GL_TEXTURE_2D, texture)
            if texture in green_textures:
                glColor4f(
                    (158 / 255.0) * color[0],(219 / 255.0) * color[1],(75 / 255.0) * color[2],color[3])
            else:
                glColor4f(*color)
            glBegin(GL_QUADS)
            for j in range(4):
                tx, ty = tex_coords[j]
                vx, vy, vz = vertices[surfaces[i][j]]
                glTexCoord2f(tx, ty)
                glVertex3f(vx, vy, vz)
            glEnd()

def place_block(name, x, y, z, color=[1,1,1,1]):
    global chunk
    data=models.get_model(name)
    texture_names = data["textures"]
    textures = []
    if isinstance(texture_names, dict):
        key_map = ["down","up","north","east","south","west"]
        for key in key_map:
            tex_name = texture_names.get(key)
            if tex_name in TEXTURE_MAP:
                textures.append(TEXTURE_MAP[tex_name])
            else:
                textures.append(TEXTURE_MAP[list(texture_names.values())[0]])
    elif isinstance(texture_names, list):
        for tex_name in texture_names:
            textures.append(TEXTURE_MAP[tex_name])
        while len(textures) < 6:
            textures.append(textures[0])
    else:
        textures = [TEXTURE_MAP[texture_names]]*6
    surfaces = [
        (0,1,2,3),
        (7,6,5,4),
        (4,5,1,0),
        (5,6,2,1),
        (6,7,3,2),
        (7,4,0,3)
    ]
    draw_block(
        cube_vertices(x*2, y*2, z*2),
        surfaces,
        [(0,0),(1,0),(1,1),(0,1)],
        textures,
        x, y, z,
        color
    )

def get_block(x,y,z):
    global chunk
    try:
        return chunk[(x,y,z)]
    except:
        return "air"
cube_surfaces = [
        (0,1,2,3),
        (7,6,5,4),
        (4,5,1,0),
        (5,6,2,1),
        (6,7,3,2),
        (7,4,0,3)
]

tex_coords = [(0,0),(1,0),(1,1),(0,1)]

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