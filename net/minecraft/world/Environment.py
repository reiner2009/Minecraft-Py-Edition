from net.minecraft.textures.Textures import *

px = load_texture("assets/minecraft/textures/environment/px.png")
nx = load_texture("assets/minecraft/textures/environment/nx.png")
py = load_texture("assets/minecraft/textures/environment/py.png")
ny = load_texture("assets/minecraft/textures/environment/ny.png")
pz = load_texture("assets/minecraft/textures/environment/pz.png")
nz = load_texture("assets/minecraft/textures/environment/nz.png")
clouds=load_texture("assets/minecraft/textures/environment/clouds.png")
clouds_z=0

t = 1
dnt=0
direction = -1

def set_tick_0():
    global t, dnt, direction
    dnt=0
    t=1
    direction = -1

def tick():
    global t, direction, dnt
    dnt += 1
    if dnt >= 60*60*5:
        t += 0.0001 * direction
    if t >= 1 and dnt >= 60*60*5:
        direction = -1
        dnt=0
    if t <= 0.1 and dnt >= 60*60*5:
        direction = 1
        dnt=0

def get_tick():
    global t
    return t

def cube_vertices(x, y, z):
    return [
        (-1+x,-1+y,-1+z), (1+x,-1+y,-1+z), (1+x,-1+y,1+z), (-1+x,-1+y,1+z),
        (-1+x,1+y,-1+z),  (1+x,1+y,-1+z),  (1+x,1+y,1+z),  (-1+x,1+y,1+z)
    ]

def cloud_vertices(x, z):
    return [(-2048+x, 300, -2048+z),(2048+x, 300, -2048+z),(2048+x,300,2048+z),(-2048+x, 300, 2048+z)]

def render(x, y, z, light=1):
    global clouds_z
    clouds_z+=0.004
    x=x*2
    y=y*2
    z=z*2
    glDisable(GL_CULL_FACE)
    glDepthMask(GL_FALSE)
    vertices = cube_vertices(x, y, z)
    surfaces = [
        (0, 1, 2, 3),
        (7, 6, 5, 4),
        (4, 5, 1, 0),
        (5, 6, 2, 1),
        (6, 7, 3, 2),
        (7, 4, 0, 3)
    ]
    textures=[ny, py, nz, pz, nx, px]
    glEnable(GL_TEXTURE_2D)
    tex_coords=[(0,0),(1,0),(1,1),(0,1)]
    glColor3f(light, light, light)
    for i in range(6):
        texture = textures[i] if i < len(textures) else textures[0]
        glBindTexture(GL_TEXTURE_2D, texture)
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[j]
            vx, vy, vz = vertices[surfaces[i][j]]
            glTexCoord2f(tx, ty)
            glVertex3f(vx, vy, vz)
        glEnd()
    glDepthMask(GL_TRUE)
    glBindTexture(GL_TEXTURE_2D, clouds)
    glBegin(GL_QUADS)
    for i in range(4):
        tx, ty = tex_coords[i]
        glTexCoord2f(tx, ty)
        glVertex3f(*cloud_vertices(0, clouds_z-4096)[i])
    glEnd()
    glBegin(GL_QUADS)
    for i in range(4):
        tx, ty = tex_coords[i]
        glTexCoord2f(tx, ty)
        glVertex3f(*cloud_vertices(0, clouds_z-4096*2)[i])
    glEnd()
    glBegin(GL_QUADS)
    for i in range(4):
        tx, ty = tex_coords[i]
        glTexCoord2f(tx, ty)
        glVertex3f(*cloud_vertices(0, clouds_z)[i])
    glEnd()
    glEnable(GL_CULL_FACE)