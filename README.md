# Minecraft-like Game in Python

A simple Minecraft-inspired 3D game built with Python.  
This project is a learning-focused implementation using OpenGL for rendering and Pygame for input handling.

---

## About the Project

This is a basic voxel-style sandbox game written in Python using PyOpenGL.

When the game starts, the player does not enter a procedurally generated world. Instead, a small predefined scene is loaded, consisting of a house and a garden.

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

Please note that you have Python 3.12 or newer installed

```bash id="install1"
git clone https://github.com/reiner2009/Minecraft-Py-Edition.git
cd Minecraft-Py-Edition
pip install -r requirements.txt
cd src
python -m net.minecraft.client.Main
