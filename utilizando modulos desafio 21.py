#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3.MP3')
pygame.mixer.music.play()
input()
pygame.event.wait()
