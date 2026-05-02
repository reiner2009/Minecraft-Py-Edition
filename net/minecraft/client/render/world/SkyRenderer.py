from net.minecraft.textures.Textures import *

px = load_texture("assets/minecraft/textures/environment/px.png")
nx = load_texture("assets/minecraft/textures/environment/nx.png")
py = load_texture("assets/minecraft/textures/environment/py.png")
ny = load_texture("assets/minecraft/textures/environment/ny.png")
pz = load_texture("assets/minecraft/textures/environment/pz.png")
nz = load_texture("assets/minecraft/textures/environment/nz.png")
pxs = load_texture("assets/minecraft/textures/environment/pxs.png")
nxs = load_texture("assets/minecraft/textures/environment/nxs.png")
pys = load_texture("assets/minecraft/textures/environment/pys.png")
nys = load_texture("assets/minecraft/textures/environment/nys.png")
pzs = load_texture("assets/minecraft/textures/environment/pzs.png")
nzs = load_texture("assets/minecraft/textures/environment/nzs.png")
clouds=load_texture("assets/minecraft/textures/environment/clouds.png")
sun=load_texture("assets/minecraft/textures/environment/sun.png")
clouds_z=0

def cube_vertices(x, y, z):
    return [
        (-1+x,-1+y,-1+z), (1+x,-1+y,-1+z), (1+x,-1+y,1+z), (-1+x,-1+y,1+z),
        (-1+x,1+y,-1+z),  (1+x,1+y,-1+z),  (1+x,1+y,1+z),  (-1+x,1+y,1+z)
    ]

def scube_vertices(x, y, z):
    return [
        (-0.9+x,-0.9+y,-0.9+z), (0.9+x,-0.9+y,-0.9+z), (0.9+x,-0.9+y,0.9+z), (-0.9+x,-0.9+y,0.9+z),
        (-0.9+x,0.9+y,-0.9+z),  (0.9+x,0.9+y,-0.9+z),  (0.9+x,0.9+y,0.9+z),  (-0.9+x,0.9+y,0.9+z)
    ]

def cloud_vertices(x, z):
    return [(-2048+x, 300, -2048+z),(2048+x, 300, -2048+z),(2048+x,300,2048+z),(-2048+x, 300, 2048+z)]

def sun_vertices():
    return [(-0.03, 0.4, -0.03),(0.03, 0.4, -0.03),(0.03,0.4,0.03),(-0.03, 0.4, 0.03)]

def render(x, y, z, light, sunriseblend, sunsetblend, t):
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
    textures = [ny, py, nx, pz, px, nz]
    sunsettextures=[nys, pys, nxs, pzs, pxs, nzs]
    sunrisetextures=[nys, pys, pxs, nzs, nxs, pzs]
    glEnable(GL_TEXTURE_2D)
    tex_coords=[(0,0),(1,0),(1,1),(0,1)]
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(light, light, light, 0.999)
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
    vertices=scube_vertices(x, y, z)
    glColor4f(light, light, light, sunriseblend)
    for i in range(6):
        texture = sunrisetextures[i] if i < len(textures) else textures[0]
        glBindTexture(GL_TEXTURE_2D, texture)
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[j]
            vx, vy, vz = vertices[surfaces[i][j]]
            glTexCoord2f(tx, ty)
            glVertex3f(vx, vy, vz)
        glEnd()
    glColor4f(light, light, light, sunsetblend)
    for i in range(6):
        texture = sunsettextures[i] if i < len(textures) else textures[0]
        glBindTexture(GL_TEXTURE_2D, texture)
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[j]
            vx, vy, vz = vertices[surfaces[i][j]]
            glTexCoord2f(tx, ty)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPushMatrix()
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, sun)
    glTranslatef(x, y, z)
    glRotatef(t-90, 0, 0, 1)
    glTranslatef(0, 0.4, 0)
    vertices = sun_vertices()
    glBegin(GL_QUADS)
    for i in range(4):
        tx, ty = tex_coords[i]
        glTexCoord2f(tx, ty)
        glVertex3f(*vertices[i])
    glEnd()
    glPopMatrix()
    glDepthMask(GL_TRUE)
    glEnable(GL_ALPHA_TEST)
    glBindTexture(GL_TEXTURE_2D, clouds)
    glColor4f(light, light, light,0.8)
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
    glDisable(GL_BLEND)
    glDisable(GL_ALPHA_TEST)