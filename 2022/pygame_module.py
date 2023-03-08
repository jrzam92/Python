
# Modules in the Pygame Package
#  Module Name                Purpose
# + pygame.cdrom           Accesses and controls CD drives
# + pygame.cursors           Loads cursor images
# + pygame.display           Accesses the display
# + pygame.draw           Draws shapes, lines, and points
# + pygame.event           Manages external events
# + pygame.font           Uses system fonts
# + pygame.image           Loads and saves an image
# + pygame.joystick           Uses joysticks and similar devices
# + pygame.key           Reads key presses from the keyboard
# + pygame.mixer           Loads and plays sounds
# + pygame.mouse           Manages the mouse
# + pygame.movie           Plays movie files
# + pygame.music           Works with music and streaming audio
# + pygame.overlay           Accesses advanced video overlays
# + pygame Contains           high-level Pygame functions
# + pygame.rect           Manages rectangular areas
# + pygame.sndarray           Manipulates sound data
# + pygame.sprite           Manages moving images
# + pygame.surface           Manages images and the screen
# + pygame.surfarray           Manipulates image pixel data
# + pygame.time           Manages timing and frame rate
# + pygame.transform           Resizes and moves images

import pygame
print(pygame.ver)
#Forma de tener pygame instalado 

#Step 1, Get a C/C++ compiler
#py -m pip install setuptools -U
#set DISTUTILS_USE_SDK=1
#set MSSdk=1
#git clone https://github.com/pygame/pygame.git
#cd pygame
#py -m pip install setuptools requests wheel numpy -U
#py -m buildconfig --download
#py -m pip install .
#py -m pygame.examples.aliens