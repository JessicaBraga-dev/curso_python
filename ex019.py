import pygame

pygame.init()
pygame.mixer.music.load("ex014.mp3")
pygame.mixer.music.play()
pygame.event.wait()