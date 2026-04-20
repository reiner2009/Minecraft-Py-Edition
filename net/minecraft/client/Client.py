import os
import contextlib
with open(os.devnull, 'w') as f, contextlib.redirect_stdout(f):
    import pygame
    from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from screeninfo import get_monitors

hud_=True
width, height=0,0
clock=None
pygame.mixer.pre_init(frequency=44100, size=16, channels=2, buffer=4096)
pygame.init()
pygame.mixer.init()
icon_surface = pygame.image.load("assets/minecraft/textures/minecraftlogo.png")
pygame.display.set_icon(icon_surface)
pygame.display.set_caption("Minecraft loading...")
for m in get_monitors():
    pygame.display.set_mode((m.width, m.height), DOUBLEBUF | OPENGL|  pygame.FULLSCREEN,vsync=1)
width, height = pygame.display.get_surface().get_size()
clock = pygame.time.Clock()
glEnable(GL_DEPTH_TEST)
glViewport(0, 0, width, height)
glDepthFunc(GL_LESS)
glEnable(GL_TEXTURE_2D)
glEnable(GL_CULL_FACE)
glCullFace(GL_BACK)
glFrontFace(GL_CCW)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(70, width / height, 0.1, 2000.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

def setup_perspective():
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70, width / height, 0.1, 2000.0)
    glMatrixMode(GL_MODELVIEW)

def setup_ortho():
    glDisable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
