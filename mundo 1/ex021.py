
"""
Faça um programa que abra e reproduza o áudio de um arquivo MP3.
"""
import pygame
pygame.init()
pygame.mixer.music.load('ex021song.mp3')
pygame.mixer.music.play()
print('\033[1:35m\nPress "enter" to stop')
input()
pygame.event.wait()

