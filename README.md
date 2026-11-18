##Minecraft-like Game in Python

A simple Minecraft-inspired 3D game built with Python.
This project is a learning-focused implementation using OpenGL for rendering and Pygame for input handling.

⸻

About the Project

This is a basic voxel-style sandbox game written in Python using PyOpenGL.

When the game starts, the player enters a procedurally generated world.

The main goal of this project is to learn:

* 3D rendering with OpenGL
* Camera and player movement systems
* Input handling with Pygame
* Basic game architecture in Python

⸻

##Features

* 3D rendering using PyOpenGL
* Camera movement
* Procedurally generated world
* Basic interaction system (if implemented)
* Window and resolution handling
* FPS-style controls
* Block classes
* Entity classes
* Support for mods, datapacks and resourcepacks

⸻

##Download and Installation

There are two ways to get and run the game:

#Option 1: Download the Source Code

If you want to explore the code, modify the game or run it using Python, you can download the source code from this repository.

Requirements:

* Python 3.10 or newer

git clone https://github.com/reiner2009/Minecraft-Py-Edition.git
cd Minecraft-Py-Edition
pip install -r requirements.txt
python -m net.minecraft.client.Main

#Option 2: Download a Prebuilt Executable

If you don’t want to install Python or set up the dependencies yourself, you can download a prebuilt executable.

Check the Releases section of this GitHub repository for available executable versions.

Simply download the version for your operating system and run it.

⸻

#Command-Line Arguments

The arguments --skin and --username are optional.

* --username: Sets your player name.
* --skin: Sets your player skin by specifying its file path. If you only specify the filename, the image must be located in the repository root directory.

Important: The skin image must have a 1:1 aspect ratio. Otherwise, it may not display correctly.

You can also use --online-skin to load another player’s skin. For example:

python -m net.minecraft.client.Main --online-skin Dream

⸻

##Controls

* Move with WASD
* Place blocks with a right-click and mine them with a left-click.
* Scroll or press the number keys to switch the block in the bottom bar.
* Press E to get more blocks.
* Press F5 to see yourself.
* Press F2 to take a screenshot. These are saved in %AppData%\.minecraft-py\screenshots\ on Windows and in $HOME/.minecraft-py/screenshots/ on other systems.
* Press F1 to hide your GUI and V to hide the block preview.