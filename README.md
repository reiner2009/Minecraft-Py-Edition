# Minecraft-like Game in Python

A simple Minecraft-inspired 3D game built with Python.  
This project is a learning-focused implementation using OpenGL for rendering and Pygame for input handling.

---

## About the Project

This is a basic voxel-style sandbox game written in Python using PyOpenGL.

When the game starts, the player enter a procedurally generated world.

The main goal of this project is to learn:
- 3D rendering with OpenGL
- Camera and player movement systems
- Input handling with Pygame
- Basic game architecture in Python

---

## Features

- 3D rendering using PyOpenGL
- First-person camera movement
- Predefined world (house + garden scene)
- Basic interaction system (if implemented)
- Window and resolution handling
- FPS-style controls

---

## Installing and Running

Please note that you have Python 3.10 or newer installed

```bash id="install1"
git clone https://github.com/reiner2009/Minecraft-Py-Edition.git
cd Minecraft-Py-Edition
pip install -r requirements.txt
python -m net.minecraft.client.Main
```

The program arguments —skin and —username are not required, but with them you can set your own player name and skin, with the skin you specify the path, if you only specify the file name, the image file must be in the root of the repository. It is important that the skin has an aspect ratio of 1:1, otherwise it is bugged.With --online-skin you can use another player's skin, e.g. with --online-skin Dream you have Dream's skin.
