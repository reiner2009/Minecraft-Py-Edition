import net.minecraft.text.Text as text
from net.minecraft.client.Client import *
import math

from net.minecraft.textures.Textures import load_texture


def cos(i):
    return math.cos(math.radians(i))
def sin(i):
    return math.sin(math.radians(i))

skin_texture = load_texture("assets/minecraft/textures/entity/player/steve.png")

def cube_vertices_head(x, y, z, yaw):
    yaw0=yaw-45
    yaw1=yaw0+90
    yaw2=yaw1+90
    yaw3=yaw2+90
    return [
        (cos(yaw0) * 0.7 + x, -cos(45) * 0.7 + y, sin(yaw0) * 0.7 + z),
        (cos(yaw1) * 0.7 + x, -cos(45) * 0.7 + y, sin(yaw1) * 0.7 + z),
        (cos(yaw2) * 0.7 + x, -cos(45) * 0.7 + y, sin(yaw2) * 0.7 + z),
        (cos(yaw3) * 0.7 + x, -cos(45) * 0.7 + y, sin(yaw3) * 0.7 + z),
        (cos(yaw0) * 0.7 + x, cos(45) * 0.7 + y, sin(yaw0) * 0.7 + z),
        (cos(yaw1) * 0.7 + x, cos(45) * 0.7 + y, sin(yaw1) * 0.7 + z),
        (cos(yaw2) * 0.7 + x, cos(45) * 0.7 + y, sin(yaw2) * 0.7 + z),
        (cos(yaw3) * 0.7 + x, cos(45) * 0.7 + y, sin(yaw3) * 0.7 + z)
    ]

def cube_vertices_body(x, y, z, yaw):
    yaw += 90
    w = 0.25
    d = 0.491
    h = 0.75
    local = [
        (-w, -h, -d),
        ( w, -h, -d),
        ( w, -h,  d),
        (-w, -h,  d),
        (-w,  h, -d),
        ( w,  h, -d),
        ( w,  h,  d),
        (-w,  h,  d),
    ]
    cy = cos(yaw)
    sy = sin(yaw)
    vertices = []
    for lx, ly, lz in local:
        rx = lx * cy - lz * sy
        rz = lx * sy + lz * cy
        vertices.append((rx + x, ly + y+0.26, rz + z))
    return vertices

def cube_vertices_arm_and_leg(x, y, z, yaw):
    yaw += 90
    w = 0.25
    d = 0.25
    h = 0.75
    local = [
        (-w, -h, -d),
        ( w, -h, -d),
        ( w, -h,  d),
        (-w, -h,  d),
        (-w,  h, -d),
        ( w,  h, -d),
        ( w,  h,  d),
        (-w,  h,  d),
    ]
    cy = cos(yaw)
    sy = sin(yaw)
    vertices = []
    for lx, ly, lz in local:
        rx = lx * cy - lz * sy
        rz = lx * sy + lz * cy
        vertices.append((rx + x, ly + y+0.26, rz + z))
    return vertices

surfaces = [
        (0,1,2,3),
        (7,6,5,4),
        (4,5,1,0),
        (5,6,2,1),
        (6,7,3,2),
        (7,4,0,3)
]

#textures=[down_texture,up_texture,left_texture,back_texture,right_texture, face_texture]

tex_coords = [
    [(16,8),(16, 0),(24, 0),(24, 8)],
    [(8,8),(8, 0),(16, 0),(16, 8)],
    [(8, 8),(0, 8),(0,16),(8, 16)],
    [(32, 8),(24, 8),(24,16),(32, 16)],
    [(24, 8),(16, 8),(16,16),(24, 16)],
    [(16, 8),(8, 8),(8,16),(16, 16)],

    [(28, 20), (28, 16), (36, 16), (36, 20)],
    [(20, 20), (20, 16), (28, 16), (28, 20)],
    [(20, 20), (16, 20), (16, 32), (20, 32)],
    [(40, 20), (32, 20), (32, 32), (40, 32)],
    [(28, 20), (24, 20), (24, 32), (28, 32)],
    [(28, 20), (20, 20), (20, 32), (28, 32)],

    [(48,20),(48, 16),(52, 16),(52, 20)],
    [(44,20),(44, 16),(48, 16),(48, 20)],
    [(44,20),(40, 20),(40, 32),(44, 32)],
    [(48,20),(44, 20),(44, 32),(48, 32)],
    [(52,20),(48, 20),(48, 32),(52, 32)],
    [(56,20),(52, 20),(52, 32),(56, 32)],

    [(48,20),(48, 16),(52, 16),(52, 20)],
    [(44,20),(44, 16),(48, 16),(48, 20)],
    [(52,20),(48, 20),(48, 32),(52, 32)],
    [(48,20),(44, 20),(44, 32),(48, 32)],
    [(44,20),(40, 20),(40, 32),(44, 32)],
    [(56,20),(52, 20),(52, 32),(56, 32)],

    [(8, 20), (8, 16), (12, 16), (12, 20)],
    [(4, 20), (4, 16), (8, 16), (8, 20)],
    [(4, 20), (0, 20), (0, 32), (4, 32)],
    [(8, 20), (4, 20), (4, 32), (8, 32)],
    [(12, 20), (8, 20), (8, 32), (12, 32)],
    [(16, 20), (12, 20), (12, 32), (16, 32)],

    [(8, 20), (8, 16), (12, 16), (12, 20)],
    [(4, 20), (4, 16), (8, 16), (8, 20)],
    [(12, 20), (8, 20), (8, 32), (12, 32)],
    [(8, 20), (4, 20), (4, 32), (8, 32)],
    [(4, 20), (0, 20), (0, 32), (4, 32)],
    [(16, 20), (12, 20), (12, 32), (16, 32)]
]

def render_body_layer(x,y,z, yaw,name_tag_is_visible, name):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, skin_texture)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[i][j]
            vx, vy, vz = cube_vertices_head(x*2, y*2+0.47, z*2, yaw)[surfaces[i][j]]
            glTexCoord2f(tx/64, ty/64)
            glVertex3f(vx, vy, vz)
        glEnd()
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx,ty=tex_coords[i+6][j]
            vx, vy, vz = cube_vertices_body(x*2, y*2-1.03, z*2, yaw)[surfaces[i][j]]
            glTexCoord2f(tx/64, ty/64)
            glVertex3f(vx, vy, vz)
        glEnd()
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx,ty=tex_coords[i+12][j]
            vx, vy, vz = cube_vertices_arm_and_leg(x*2+cos(yaw)*0.74, y*2-1.03, z*2+sin(yaw)*0.74, yaw)[surfaces[i][j]]
            glTexCoord2f(tx/64, ty/64)
            glVertex3f(vx, vy, vz)
        glEnd()
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx,ty=tex_coords[i+18][j]
            vx, vy, vz = cube_vertices_arm_and_leg(x*2-cos(yaw)*0.74, y*2-1.03, z*2-sin(yaw)*0.74, yaw)[surfaces[i][j]]
            glTexCoord2f(tx/64, ty/64)
            glVertex3f(vx, vy, vz)
        glEnd()
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx,ty=tex_coords[i+24][j]
            vx, vy, vz = cube_vertices_arm_and_leg(x*2+cos(yaw)*0.25, y*2-2.53, z*2+sin(yaw)*0.25, yaw)[surfaces[i][j]]
            glTexCoord2f(tx/64, ty/64)
            glVertex3f(vx, vy, vz)
        glEnd()
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx,ty=tex_coords[i+30][j]
            vx, vy, vz = cube_vertices_arm_and_leg(x*2-cos(yaw)*0.245, y*2-2.53, z*2-sin(yaw)*0.25, yaw)[surfaces[i][j]]
            glTexCoord2f(tx/64, ty/64)
            glVertex3f(vx, vy, vz)
        glEnd()
    if name_tag_is_visible:
        text.render_text_billboard(name, x*2,y*2+1,z*2,0.5,0.3)