import os
import sys
if sys.platform == "darwin":
    os.environ["PYOPENGL_PLATFORM"] = "darwin"
elif sys.platform.startswith("linux"):
    os.environ["PYOPENGL_PLATFORM"] = "glx"
from OpenGL.GL import *
import glfw
import net.mcpy.client.renderer.Renderer as Renderer
import net.mcpy.client.GameClient as GameClient
import net.mcpy.client.input.InputHandler as InputHandler
import net.mcpy.client.AtlasManager as AtlasManager
import net.mcpy.game.Minecraft as Minecraft
import net.mcpy.client.renderer.world.block.Models as BlockModels
import net.mcpy.game.GameTickThread as GameTickThread


window = None
width = None
height = None

def init():
    global window, width, height
    Minecraft.init()
    if not glfw.init():
        raise RuntimeError("Failed to load GLFW")
    monitor = glfw.get_primary_monitor()
    videoMode = glfw.get_video_mode(monitor)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
    width = videoMode.size.width
    height = videoMode.size.height
    GameClient.attributes["resolution"]=[width, height]
    window = glfw.create_window(
        width, height,
        "MinecraftPy-Client",
        monitor,
        None
    )
    GameClient.attributes["window"]=window
    if window is None:
        glfw.terminate()
        raise RuntimeError("Failed to create window")
    glfw.make_context_current(window)
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
    InputHandler.registerCallbacks()
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    glFrontFace(GL_CCW)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glDisable(GL_BLEND)
    glViewport(0, 0, width, height)
    glEnable(GL_TEXTURE_2D)
    glClearColor(0,0,1,1)
    glfw.swap_interval(1)
    glfw.show_window(window)
    AtlasManager.init()
    GameClient.init()
    BlockModels.init()
    Renderer.init()
    GameTickThread.client_tick_thread.start()

def render():
    while not glfw.window_should_close(window):
        glfw.poll_events()
        Renderer.render()
        InputHandler.handleInput()
        glfw.swap_buffers(window)

def shutdown():
    glfw.destroy_window(window)
    glfw.terminate()
