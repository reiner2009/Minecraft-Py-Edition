import net.minecraft.text.Text as text
from net.minecraft.world.block.Block import *
import math


def cos(i):
    return math.cos(math.radians(i))
def sin(i):
    return math.sin(math.radians(i))


block_tex_coords=[(0,0),(1,0),(1,1),(0,1)]

def item_vertices():
    return [
        (-0.5, 1.3, -0.5), (0, 1.3, -0.5), (0, 1.3, 0), (-0.5, 1.3, 0),
        (-0.5, 0.8, -0.5), (0, 0.8, -0.5), (0, 0.8, 0), (-0.5, 0.8, 0)
    ]

def cube_vertices_head():
    return [
        (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
        (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)
    ]

def cube_vertices_body():
    return [
        (-0.25, -0.75, -0.491), (0.25, -0.75, -0.491), (0.25, -0.75, 0.491), (-0.25, -0.75, 0.491),
        (-0.25, 0.75, -0.491), (0.25, 0.75, -0.491), (0.25, 0.75, 0.491), (-0.25, 0.75, 0.491)
    ]

def cube_vertices_arm_and_leg():
    return [
        (-0.25, 1.5, -0.25), (0.25, 1.5, -0.25), (0.25, 1.5, 0.25), (-0.25, 1.5, 0.25),
        (-0.25, 0, -0.25), (0.25, 0, -0.25), (0.25, 0, 0.25), (-0.25, 0, 0.25)
    ]

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
    [(52,20),(48, 20),(48, 32),(52, 32)],
    [(48,20),(44, 20),(44, 32),(48, 32)],
    [(44,20),(40, 20),(40, 32),(44, 32)],
    [(56,20),(52, 20),(52, 32),(56, 32)],

    [(40, 52), (40, 48), (44, 48), (44, 52)],
    [(36, 52), (36, 48), (40, 48), (40, 52)],
    [(44, 52), (40, 52), (40, 64), (44, 64)],
    [(40, 52), (36, 52), (36, 64), (40, 64)],
    [(36, 52), (32, 52), (32, 64), (36, 64)],
    [(48, 52), (44, 52), (44, 64), (48, 64)],

    [(8, 20), (8, 16), (12, 16), (12, 20)],
    [(4, 20), (4, 16), (8, 16), (8, 20)],
    [(4, 20), (0, 20), (0, 32), (4, 32)],
    [(8, 20), (4, 20), (4, 32), (8, 32)],
    [(12, 20), (8, 20), (8, 32), (12, 32)],
    [(16, 20), (12, 20), (12, 32), (16, 32)],

    [(24, 52), (24, 48), (28, 48), (28, 52)],
    [(20, 52), (20, 48), (24, 48), (24, 52)],
    [(20, 52), (16, 52), (16, 64), (20, 64)],
    [(24, 52), (20, 52), (20, 64), (24, 64)],
    [(28, 52), (24, 52), (24, 64), (28, 64)],
    [(32, 52), (28, 52), (28, 64), (32, 64)],

    [(48,8),(48, 0),(56, 0),(56, 8)],
    [(40,8),(40, 0),(48, 0),(48, 8)],
    [(40, 8),(32, 8),(32,16),(40, 16)],
    [(64, 8),(56, 8),(56,16),(64, 16)],
    [(56, 8),(48, 8),(48,16),(56, 16)],
    [(48, 8),(40, 8),(40,16),(48, 16)],

    [(48, 36),(48, 32),(52, 32),(52, 36)],
    [(44, 36),(44, 32),(48, 32),(48, 36)],
    [(52, 36),(48, 36),(48, 48),(52, 48)],
    [(48, 36),(44, 36),(44, 48),(48, 48)],
    [(44, 36),(40, 36),(40, 48),(44, 48)],
    [(56, 36),(52, 36),(52, 48),(56, 48)],

    [(56, 52), (56, 48), (60, 48), (60, 52)],
    [(52, 52), (52, 48), (56, 48), (56, 52)],
    [(60, 52), (56, 52), (56, 64), (60, 64)],
    [(56, 52), (52, 52), (52, 64), (56, 64)],
    [(52, 52), (48, 52), (48, 64), (52, 64)],
    [(64, 52), (60, 52), (60, 64), (64, 64)],

    [(28, 36), (28, 32), (36, 32), (36, 36)],
    [(20, 36), (20, 32), (28, 32), (28, 36)],
    [(20, 36), (16, 36), (16, 48), (20, 48)],
    [(40, 36), (32, 36), (32, 48), (40, 48)],
    [(28, 36), (24, 36), (24, 48), (28, 48)],
    [(28, 36), (20, 36), (20, 48), (28, 48)],

    [(8, 36), (8, 32), (12, 32), (12, 36)],
    [(4, 36), (4, 32), (8, 32), (8, 36)],
    [(4, 36), (0, 36), (0, 48), (4, 48)],
    [(8, 36), (4, 36), (4, 48), (8, 48)],
    [(12, 36), (8, 36), (8, 48), (12, 48)],
    [(16, 36), (12, 36), (12, 48), (16, 48)],

    [(8, 52), (8, 48), (12, 48), (12, 52)],
    [(4, 52), (4, 48), (8, 48), (8, 52)],
    [(4, 52), (0, 52), (0, 64), (4, 64)],
    [(8, 52), (4, 52), (4, 64), (8, 64)],
    [(12, 52), (8, 52), (8, 64), (12, 64)],
    [(16, 52), (12, 52), (12, 64), (16, 64)],
]

def render_arms(x,y,z, yaw,left_arm_pitch,right_arm_pitch, block_name, skin_texture):
    glEnable(GL_ALPHA_TEST)
    glDisable(GL_CULL_FACE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D,skin_texture)
    glPushMatrix()
    glTranslatef(x * 2 - cos(yaw) * 0.74, y * 2 - 1.52, z * 2 - sin(yaw) * 0.74)
    glTranslatef(0, 2.0, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, -0.5, 0)
    glRotatef(left_arm_pitch, 0.0, 0.0, 1.0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[i + 12][j]
            vx, vy, vz = cube_vertices_arm_and_leg()[surfaces[i][j]]
            glTexCoord2f(tx / 64, ty / 64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(x * 2 + cos(yaw) * 0.74, y * 2 - 1.52, z * 2 + sin(yaw) * 0.74)
    glTranslatef(0, 2.0, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, -0.5, 0)
    glRotatef(right_arm_pitch, 0.0, 0.0, 1.0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[i + 18][j]
            vx, vy, vz = cube_vertices_arm_and_leg()[surfaces[i][j]]
            glTexCoord2f(tx / 64, ty / 64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(x * 2 - cos(yaw) * 0.74, y * 2 - 1.52, z * 2 - sin(yaw) * 0.74)
    glTranslatef(0, 2.0, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, -0.5, 0)
    glRotatef(left_arm_pitch, 0.0, 0.0, 1.0)
    glTranslatef(0, 0.5, 0)
    glScalef(1.05, 1.05, 1.05)
    glTranslatef(0, -0.5, 0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[i + 42][j]
            vx, vy, vz = cube_vertices_arm_and_leg()[surfaces[i][j]]
            glTexCoord2f(tx / 64, ty / 64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(x * 2 + cos(yaw) * 0.74, y * 2 - 1.52, z * 2 + sin(yaw) * 0.74)
    glTranslatef(0, 2.0, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, -0.5, 0)
    glRotatef(right_arm_pitch, 0.0, 0.0, 1.0)
    glTranslatef(0, 0.5, 0)
    glScalef(1.05, 1.05, 1.05)
    glTranslatef(0, -0.5, 0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[i + 48][j]
            vx, vy, vz = cube_vertices_arm_and_leg()[surfaces[i][j]]
            glTexCoord2f(tx / 64, ty / 64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    try:
        glPushMatrix()
        glTranslatef(x * 2 + cos(yaw-45), y * 2 - 1.52, z * 2 + sin(yaw-45))
        glTranslatef(0, 2.0, 0)
        glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
        glTranslatef(0, -0.5, 0)
        glRotatef(right_arm_pitch, 0.0, 0.0, 1.0)
        data = models.get_model(block_name)
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
        for i in range(6):
            texture = textures[i] if i < len(textures) else textures[0]
            glBindTexture(GL_TEXTURE_2D, texture)
            glBegin(GL_QUADS)
            for j in range(4):
                tx, ty = block_tex_coords[j]
                vx, vy, vz = item_vertices()[surfaces[i][j]]
                glTexCoord2f(tx, ty)
                glVertex3f(vx, vy, vz)
            glEnd()
    except KeyError:
        pass
    finally:
        glPopMatrix()


def render_body_layer(x,y,z, yaw, pitch,left_arm_pitch,right_arm_pitch, walk_pitch_0, walk_pitch_1,name_tag_is_visible, name, block_name, skin_texture):
    glDisable(GL_CULL_FACE)
    glEnable(GL_ALPHA_TEST)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, skin_texture)
    glPushMatrix()
    glTranslatef(x*2, y*2+0.48, z*2)
    glTranslatef(0,0.5,0)
    glRotatef(-yaw-90, 0.0, 1.0, 0.0)
    glTranslatef(0, -0.5, 0)
    glRotatef(pitch, 0.0, 0.0, 1.0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[i][j]
            vx, vy, vz = cube_vertices_head()[surfaces[i][j]]
            glTexCoord2f(tx/64, ty/64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(x * 2, y * 2 + 0.48, z * 2)
    glTranslatef(0, 0.5, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, -0.5, 0)
    glRotatef(pitch, 0.0, 0.0, 1.0)
    glTranslatef(0,0.05, 0)
    glScalef(1.05, 1.05, 1.05)
    glTranslatef(0, -0.05, 0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[i+36][j]
            vx, vy, vz = cube_vertices_head()[surfaces[i][j]]
            glTexCoord2f(tx / 64, ty / 64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(x * 2, y * 2-0.77, z * 2)
    glTranslatef(0, 0.5, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, -0.5, 0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx,ty=tex_coords[i+6][j]
            vx, vy, vz = cube_vertices_body()[surfaces[i][j]]
            glTexCoord2f(tx/64, ty/64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(x * 2, y * 2 - 0.77, z * 2)
    glTranslatef(0, 0.5, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, -0.55, 0)
    glScalef(1.05, 1.05, 1.05)
    glTranslatef(0, 0.035, 0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[i + 54][j]
            vx, vy, vz = cube_vertices_body()[surfaces[i][j]]
            glTexCoord2f(tx / 64, ty / 64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    render_arms(x,y,z,yaw, left_arm_pitch,right_arm_pitch, block_name, skin_texture)
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, skin_texture)
    glTranslatef(x * 2 - cos(yaw) * 0.25, y * 2 - 1.52, z * 2 - sin(yaw) * 0.25)
    glTranslatef(0, 0, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, 0, 0)
    glRotatef(walk_pitch_0, 0.0, 0.0, 1.0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx,ty=tex_coords[i+24][j]
            vx, vy, vz = cube_vertices_arm_and_leg()[surfaces[i][j]]
            glTexCoord2f(tx/64, ty/64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(x * 2 + cos(yaw) * 0.25, y * 2 - 1.52, z * 2 + sin(yaw) * 0.25)
    glTranslatef(0, 0, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, 0, 0)
    glRotatef(walk_pitch_1, 0.0, 0.0, 1.0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx,ty=tex_coords[i+30][j]
            vx, vy, vz = cube_vertices_arm_and_leg()[surfaces[i][j]]
            glTexCoord2f(tx/64, ty/64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, skin_texture)
    glTranslatef(x * 2 - cos(yaw) * 0.25, y * 2 - 1.52, z * 2 - sin(yaw) * 0.25)
    glTranslatef(0, 0, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, 0, 0)
    glRotatef(walk_pitch_0, 0.0, 0.0, 1.0)
    glTranslatef(0, 0.05, 0)
    glScalef(1.05, 1.05, 1.05)
    glTranslatef(0, -0.025, 0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[i + 60][j]
            vx, vy, vz = cube_vertices_arm_and_leg()[surfaces[i][j]]
            glTexCoord2f(tx / 64, ty / 64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(x * 2 + cos(yaw) * 0.25, y * 2 - 1.52, z * 2 + sin(yaw) * 0.25)
    glTranslatef(0, 0, 0)
    glRotatef(-yaw - 90, 0.0, 1.0, 0.0)
    glTranslatef(0, 0, 0)
    glRotatef(walk_pitch_1, 0.0, 0.0, 1.0)
    glTranslatef(0, 0.05, 0)
    glScalef(1.05, 1.05, 1.05)
    glTranslatef(0, -0.025, 0)
    for i in range(6):
        glBegin(GL_QUADS)
        for j in range(4):
            tx, ty = tex_coords[i + 66][j]
            vx, vy, vz = cube_vertices_arm_and_leg()[surfaces[i][j]]
            glTexCoord2f(tx / 64, ty / 64)
            glVertex3f(vx, vy, vz)
        glEnd()
    glPopMatrix()
    if name_tag_is_visible:
        text.render_text_billboard(name, x*2,y*2+1,z*2,0.5,0.3)