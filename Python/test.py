import pygame
import time

import pygame
pygame.init()
pygame.mixer.init()
music = pygame.mixer.music
music.load("../Media/music.wav")
music.set_volume(0.3)
music.play() 

while True:
    time.sleep(1)